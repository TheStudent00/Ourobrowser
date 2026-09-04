---
id: ourobrowser.root.research
level: 1
status: draft
settled_by: Dee
supersedes: null
designation: work
node:
    name: research
    path: Planning/node_0_1_research/CORE_0_1_research.md
super_node:
    name: Ourobrowser
    path: ../CORE_0.md
sub_nodes:
    - name: pc_ingress
      path: node_0_0_pc_ingress/CORE_0_0_pc_ingress.md
    - name: pc_egress
      path: node_0_1_pc_egress/CORE_0_1_pc_egress.md
    - name: chromium_compilation
      path: node_0_2_chromium_compilation/CORE_0_2_chromium_compilation.md
    - name: runtime_embedding
      path: node_0_3_runtime_embedding/CORE_0_3_runtime_embedding.md
---

# CORE 0_1 — research

## metadata

- **id:** ourobrowser.root.research
- **level:** 1
- **status:** draft
- **designation:** work
- **settled_by:** Dee
- **supersedes:** null

## super_node

- [Ourobrowser](../CORE_0.md)

## sub_nodes

- [pc_ingress](node_0_0_pc_ingress/CORE_0_0_pc_ingress.md) — **Goal:** Configure PseudoCoup (PC) to ingress the Chromium DOM-to-V8 bindings and WebIDL definitions.
- [pc_egress](node_0_1_pc_egress/CORE_0_1_pc_egress.md) — **Goal:** Configure PC to emit CPython (or pybind11) wrappers in place of the original V8 bindings.
- [chromium_compilation](node_0_2_chromium_compilation/CORE_0_2_chromium_compilation.md) — **Goal:** Modify the Chromium build system (GN/Ninja) to compile our PC-processed bindings.
- [runtime_embedding](node_0_3_runtime_embedding/CORE_0_3_runtime_embedding.md)

## definition

This branch represents the physically separate research and execution plan for using PseudoCoup (PC) to systematically swap the V8 JavaScript engine for a local, embedded Python execution engine inside the Chromium C++ codebase. It serves as the root planning research folder for creating a standalone, Python-native browser that completely bypasses JavaScript execution.
