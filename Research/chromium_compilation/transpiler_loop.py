import sys
import os
import subprocess
import json
import shutil
import re

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
        
    ledger_data = {"types": {}}
    for v8_type, py_type in GLOBAL_TYPES.items():
        ledger_data["types"][f".{v8_type}"] = py_type
        
    ledger_data["functions"] = GLOBAL_FUNCTIONS
        
    with open(ledger_path, 'w') as f:
        json.dump(ledger_data, f, indent=4)
        
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
    if os.path.exists(out_path) and out_path != abs_path:
        shutil.move(out_path, abs_path)

files = get_failed_files()
if not files:
    print("No files to transpile!")
else:
    for f in files:
        transpile_file(f)
    print("Transpilation of failed files complete!")
