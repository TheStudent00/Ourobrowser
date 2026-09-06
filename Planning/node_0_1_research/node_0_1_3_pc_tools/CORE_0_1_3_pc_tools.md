---
id: ourobrowser.root.research.pc_tools
level: 2
status: settled
settled_by: Dee
supersedes: null
designation: code (module)
sub_nodes: []
node:
    name: pc_tools
    path: Planning/node_0_1_research/node_0_1_3_pc_tools/CORE_0_1_3_pc_tools.md
super_node:
    name: research
    path: ../CORE_0_1_research.md
---

# CORE 0_1_3 — pc_tools

## metadata

- **id:** ourobrowser.root.research.pc_tools
- **level:** 2
- **status:** settled
- **designation:** code (module)
- **settled_by:** Dee
- **supersedes:** null

## super_node

- [research](../CORE_0_1_research.md)

## sub_nodes

*(none — this is a leaf.)*

## definition

The copy of the PseudoCoup transpiler this project drives, at `Tools/PCv3.1`.
It is a clone of `PseudoCoup_v3`, kept inside this repo so the Chromium
bindings swap can change the C++ ingress and the C++ emitter without
touching the transpiler any other project builds on.

## settled

- **Implementation:** Cloned `PseudoCoup_v3` into `Tools/PCv3.1` and patched `core.ledger` and `egress.cpp` to correctly parse and respect ledger mappings (derived from PCHQ research concepts). This serves as our isolated working transpiler for the Chromium bindings swap!
