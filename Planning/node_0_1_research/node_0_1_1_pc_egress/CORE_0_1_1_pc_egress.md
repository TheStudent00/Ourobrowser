---
id: ourobrowser.root.research.pc_egress
level: 2
status: settled
settled_by: Dee
supersedes: null
designation: settled
node:
    name: pc_egress
    path: Planning/node_0_1_research/node_0_1_1_pc_egress/CORE_0_1_1_pc_egress.md
super_node:
    name: research
    path: ../CORE_0_1_research.md
sub_nodes:
    - name: emitter_config
      path: node_0_1_1_0_emitter_config/CORE_0_1_1_0_emitter_config.md
    - name: runner_script
      path: node_0_1_1_1_runner_script/CORE_0_1_1_1_runner_script.md
---

# CORE 0_1_1 — pc_egress

## metadata

- **id:** ourobrowser.root.research.pc_egress
- **level:** 2
- **status:** settled
- **designation:** settled
- **settled_by:** Dee
- **supersedes:** null

## super_node

- [research](../CORE_0_1_research.md)

## sub_nodes

- [emitter_config](node_0_1_1_0_emitter_config/CORE_0_1_1_0_emitter_config.md)
- [runner_script](node_0_1_1_1_runner_script/CORE_0_1_1_1_runner_script.md)

## definition

Configure PC to traverse the newly created UR-AST and emit Python C-API wrapper bindings in place of the original V8 bindings, generating native C++ files that seamlessly bridge Blink to CPython.

## design

**1. Target Mapping Strategy (`py_emitter_config.yaml`)**
We instruct PC's emitter to structurally map the V8 "Dead Ends" (from the Ingress Ledger) to their concrete CPython API equivalents.
```yaml
egress:
  target_lang: cpp
  type_maps:
    "v8::Isolate*": "PyInterpreterState*"
    "v8::Local<v8::Value>": "PyObject*"
    "v8::Local<v8::Context>": "PyDictObject*" # Frame execution context
    "v8::FunctionCallbackInfo": "PyObject* args" # Standard *args tuple
  class_rename_regex:
    pattern: "^V8(.*)"
    replacement: "Py\\1"
```

**2. The Egress Runner (`run_egress.sh`)**
The script to consume the UR-AST and emit the massive `PyDOM` wrapper directory.
```bash
python3 -m pseudocoup.cli \
    --ast-input ur_ast_chromium_bindings.json \
    --target-lang cpp \
    --emitter-config py_emitter_config.yaml \
    --outdir third_party/blink/renderer/bindings/core/python/
```

## settled rules
- **Memory Management Handoff:** V8 uses Garbage Collection, which Chromium integrates with via `cppgc`. Python uses Reference Counting (`Py_INCREF` / `Py_DECREF`). PC must emit explicit `Py_XDECREF` calls in the C++ destructors of the generated wrapper classes to prevent memory leaks when DOM elements are destroyed.
- **Header Emission:** No emitted file may `#include <v8.h>`. All emitted C++ files must strictly `#include <Python.h>`.
- **Naming Convention:** All auto-generated V8 files (e.g., `v8_html_button_element.cc`) must be deterministically emitted as `py_html_button_element.cc` to ensure clean integration with the GN build system later.
