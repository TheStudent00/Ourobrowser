import os
import subprocess
import json
import shutil

FAILED_FILES = [
    "../../third_party/blink/renderer/platform/bindings/binding_security_for_platform.h",
    "../../third_party/blink/renderer/platform/bindings/exception_state.h"
]

CHROMIUM_SRC = os.path.expanduser("~/Programming/chromium_src/src")
PC_V3_CLI = os.path.expanduser("~/Programming/Ourobrowser/Tools/PCv3.1/pseudocoup/cli.py")

GLOBAL_TYPES = {
    "v8::Local<v8::Context>": "PyDictObject*",
    "v8::MaybeLocal<v8::Context>": "PyDictObject*",
    "v8::Isolate*": "PyInterpreterState*",
    "v8::Local<v8::Value>": "PyObject*",
    "v8::Local<v8::Object>": "PyObject*",
    "v8::Local<v8::String>": "PyObject*"
}

def transpile_file(rel_path):
    # Remove the ninja build directory offset
    if rel_path.startswith("../../"):
        rel_path = rel_path[6:]
        
    abs_path = os.path.join(CHROMIUM_SRC, rel_path)
    ledger_path = abs_path.replace(".h", ".ledger.json").replace(".cc", ".ledger.json")
    
    # 1. Strip the #include "v8.h" (or v8/include/v8.h)
    with open(abs_path, 'r') as f:
        content = f.read()
    
    content = content.replace('#include "v8/include/v8.h"', '#include <Python.h>')
    content = content.replace('#include "v8.h"', '#include <Python.h>')
    
    # Also PCv3.1 bug: strip "namespace blink {" wrapper so the parser doesn't drop it
    content = content.replace('namespace blink {', '// namespace blink {')
    content = content.replace('}  // namespace blink', '// }  // namespace blink')
    
    with open(abs_path, 'w') as f:
        f.write(content)
        
    # 2. Write a base ledger
    ledger_data = {"types": {}}
    for v8_type, py_type in GLOBAL_TYPES.items():
        ledger_data["types"][f".{v8_type}"] = py_type # Basic hack for now
        
    with open(ledger_path, 'w') as f:
        json.dump(ledger_data, f, indent=4)
        
    # 3. Transpile!
    print(f"Transpiling {rel_path}...")
    try:
        subprocess.run(["python3", PC_V3_CLI, "--source", abs_path, "--source-lang", "cpp", "--target-lang", "cpp"], check=True, env={"PYTHONPATH": os.path.expanduser("~/Programming/Ourobrowser/Tools/PCv3.1")})
    except subprocess.CalledProcessError:
        print(f"Failed to transpile {rel_path}")
        return
        
    # PCv3.1 outputs to .cpp. We need to rename it back to the original file
    out_ext = ".cpp"
    out_path = abs_path.rsplit('.', 1)[0] + out_ext
    if os.path.exists(out_path) and out_path != abs_path:
        shutil.move(out_path, abs_path)

for f in FAILED_FILES:
    transpile_file(f)

print("Transpilation of failed files complete!")
