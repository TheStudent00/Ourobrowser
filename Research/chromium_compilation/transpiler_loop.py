import sys
import os
import subprocess
import json
import shutil
import re
from collections import Counter

# Use /projects/ paths since this runs inside the Airlock container
CHROMIUM_SRC = os.environ.get("CHROMIUM_SRC", "/projects/chromium_src/src")
PC_V3_CLI = os.environ.get("PC_V3_CLI", "/projects/Ourobrowser/Tools/PCv3.1/pseudocoup/cli.py")
PC_V3_PYTHONPATH = os.environ.get("PC_V3_PYTHONPATH", "/projects/Ourobrowser/Tools/PCv3.1")

# Written types -> Python C-API types. A key is the type exactly as it is
# written in the source, pointers and qualifiers included; PCv3.1 reads a
# declaration's full written type since 2026-09-06 (Ourobrowser log_002).
GLOBAL_TYPES = {
    "v8::Local<v8::Context>": "PyDictObject*",
    "v8::MaybeLocal<v8::Context>": "PyDictObject*",
    "v8::Isolate*": "PyInterpreterState*",
    "v8::Local<v8::Value>": "PyObject*",
    "v8::Local<v8::Object>": "PyObject*",
    "v8::Local<v8::String>": "PyObject*",
    "const v8::FunctionCallbackInfo<v8::Value>&": "PyObject*",
}

# Function calls -> Python C-API calls. `{0}`, `{1}` are the call's arguments
# in order; a key starting with `.` names a METHOD by name alone, and `{self}`
# is its receiver -- `.ToLocalChecked` -> `{self}` unwraps a v8::MaybeLocal.
GLOBAL_FUNCTIONS = {
    "v8::String::NewFromUtf8": "PyUnicode_FromString({1})",
    "v8::Isolate::GetCurrent": "PyInterpreterState_Get",
    "v8::Exception::Error": "PyErr_SetString(PyExc_RuntimeError, {0})",
    "v8::Exception::TypeError": "PyErr_SetString(PyExc_TypeError, {0})",
    ".ToLocalChecked": "{self}",
}

IDENTIFIER = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")


def name_census(text):
    """Every identifier in the text, with how many times it appears."""
    return Counter(IDENTIFIER.findall(text))


def losses(before, after):
    """Identifiers the transpile DROPPED, and how many of each.

    A name may legitimately disappear: it is the point of the exercise that
    `v8::String::NewFromUtf8` stops appearing and `PyUnicode_FromString`
    starts. So every name named on either side of a mapping is excused, and
    what is left is loss the mapping does not account for.

    This exists because a transpile that silently drops code looks exactly
    like a transpile that worked. On 2026-09-05 seven Chromium headers were
    rewritten in place down to their `#include` lines, and nothing reported
    it -- `exception_state.h` went from 274 lines to 6 and the loop went on
    to the next file. Measured, that run dropped 374 distinct identifiers
    from that one file."""
    excused = set()
    for k, v in list(GLOBAL_TYPES.items()) + list(GLOBAL_FUNCTIONS.items()):
        excused.update(IDENTIFIER.findall(k))
        excused.update(IDENTIFIER.findall(v))
    b, a = name_census(before), name_census(after)
    return {n: b[n] - a.get(n, 0) for n in b
            if b[n] > a.get(n, 0) and n not in excused}


def write_ledger(ledger_path):
    """The one place the mapping tables become a PCv3.1 ledger file. A type
    key gets a leading `.`: the ledger's global-type key for a written type
    (`.v8::Isolate*`), as opposed to a per-variable key (`Foo.isolate`)."""
    ledger_data = {"types": {f".{k}": v for k, v in GLOBAL_TYPES.items()},
                   "functions": dict(GLOBAL_FUNCTIONS)}
    with open(ledger_path, 'w') as f:
        json.dump(ledger_data, f, indent=4)


def get_failed_files():
    files = set()
    try:
        with open("ninja_errors.log", "r") as f:
            for line in f:
                line = line.strip()
                if line.startswith("../../third_party"):
                    files.add(line)
    except FileNotFoundError:
        print("ninja_errors.log not found")
    return list(files)

def transpile_file(rel_path):
    if rel_path.startswith("../../"):
        rel_path = rel_path[6:]
        
    abs_path = os.path.join(CHROMIUM_SRC, rel_path)
    ledger_path = abs_path.replace(".h", ".ledger.json").replace(".cc", ".ledger.json")
    
    if not os.path.exists(abs_path):
        print(f"Skipping {abs_path}, file does not exist")
        return

    # The file is rewritten IN PLACE. Keep the version that was there before
    # the first pass, once, so a bad pass can be undone without git.
    backup = abs_path + ".pc_orig"
    if not os.path.exists(backup):
        shutil.copy2(abs_path, backup)

    with open(abs_path, 'r') as f:
        content = f.read()

    # Only the v8 include is rewritten here. Preprocessor lines, comments and
    # export macros now pass through the transpiler unchanged (PCv3.1 carries
    # unmapped constructs as RawNode text), so they are no longer stripped or
    # re-prepended -- that re-prepending is what stacked five copies of the
    # standard-library prelude onto exception_state.h on 2026-09-05.
    content = content.replace('#include "v8/include/v8.h"', '#include <Python.h>')
    content = content.replace('#include "v8.h"', '#include <Python.h>')
    
    with open(abs_path, 'w') as f:
        f.write(content)
        
    write_ledger(ledger_path)
        
    print(f"Transpiling {rel_path}...")
    try:
        env = os.environ.copy()
        env["PYTHONPATH"] = PC_V3_PYTHONPATH
        subprocess.run([sys.executable, PC_V3_CLI, "--source", abs_path, "--source-lang", "cpp", "--target-lang", "cpp"], check=True, env=env)
    except subprocess.CalledProcessError:
        print(f"Failed to transpile {rel_path}")
        return
        
    out_ext = ".cpp"
    out_path = abs_path.rsplit('.', 1)[0] + out_ext
    if not (os.path.exists(out_path) and out_path != abs_path):
        return

    # NOTHING is written over the source until the transpile is shown not to
    # have lost anything the mapping does not account for.
    with open(backup, 'r') as f:
        original = f.read()
    with open(out_path, 'r') as f:
        produced = f.read()

    dropped = losses(original, produced)
    if dropped:
        worst = sorted(dropped.items(), key=lambda kv: -kv[1])[:8]
        print(f"REFUSED {rel_path}: the transpile dropped {len(dropped)} "
              f"identifier(s) the mapping does not account for; "
              f"worst: {worst}")
        print(f"        the file is unchanged; what was produced is at {out_path}.rejected")
        os.replace(out_path, out_path + ".rejected")
        shutil.copy2(backup, abs_path)      # undo the include rewrite too
        return

    shutil.move(out_path, abs_path)
    print(f"  wrote {rel_path}")

def main():
    files = get_failed_files()
    if not files:
        print("No files to transpile!")
        return
    for f in files:
        transpile_file(f)
    print("Transpilation of failed files complete!")


if __name__ == "__main__":
    main()
