---
id: ourobrowser.root.research.pc_egress
level: 2
status: draft
settled_by: Dee
supersedes: null
designation: pending
node:
    name: pc_egress
    path: Planning/node_0_1_research/node_0_1_pc_egress/CORE_0_1_pc_egress.md
super_node:
    name: research
    path: ../CORE_0_1_research.md
sub_nodes: []
---

# CORE 0_1 — pc_egress

## metadata

- **id:** ourobrowser.root.research.pc_egress
- **level:** 2
- **status:** draft
- **designation:** pending
- **settled_by:** Dee
- **supersedes:** null

## super_node

- [research](../CORE_0_1_research.md)

## sub_nodes

*(none yet)*

## definition

**Goal:** Configure PC to emit CPython (or pybind11) wrappers in place of the original V8 bindings.

**Details:**
- Instruct PC to swap the target architecture from V8 to Python.
- When PC traverses the UR-AST built during Ingress, it will emit new C++ binding code (`pybind11` or Python C-API native extensions) that mirror the exact DOM interface structure defined in the WebIDL.
- E.g., `blink::HTMLButtonElement` binding code is rewritten from generating a V8 object to generating a `PyObject*`.
- This ensures that Chromium's internal event loop and DOM tree seamlessly communicate with an embedded Python execution environment without realizing JavaScript is missing.
