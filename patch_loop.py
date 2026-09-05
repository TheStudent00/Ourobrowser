import re

with open('Research/chromium_compilation/transpiler_loop.py', 'r') as f:
    content = f.read()

# Add GLOBAL_FUNCTIONS
target_types = """    "v8::Local<v8::String>": "PyObject*"
}"""
replacement_types = target_types + """

GLOBAL_FUNCTIONS = {
    "v8::String::NewFromUtf8": "PyUnicode_FromString({1})",
    "v8::Isolate::GetCurrent": "PyInterpreterState_Get",
    "v8::Exception::Error": "PyErr_SetString(PyExc_RuntimeError, {0})",
    "v8::Exception::TypeError": "PyErr_SetString(PyExc_TypeError, {0})"
}"""
content = content.replace(target_types, replacement_types)

# Add to ledger generation
target_ledger = """    for v8_type, py_type in GLOBAL_TYPES.items():
        ledger_data["types"][f".{v8_type}"] = py_type"""
replacement_ledger = target_ledger + """
        
    ledger_data["functions"] = GLOBAL_FUNCTIONS"""
content = content.replace(target_ledger, replacement_ledger)

with open('Research/chromium_compilation/transpiler_loop.py', 'w') as f:
    f.write(content)
