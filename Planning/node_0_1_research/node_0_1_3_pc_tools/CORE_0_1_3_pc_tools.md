---
name: pc_tools
designation: pending
status: settled
sub_nodes: []
node:
    name: pc_tools
    path: Planning/node_0_1_research/node_0_1_3_pc_tools/CORE_0_1_3_pc_tools.md
super_node:
    name: research
    path: ../CORE_0_1_research.md
---

# node_0_2_pc_tools

## metadata

- **status:** settled
- **designation:** pending

## super_node

- [research](../CORE_0_1_research.md)

## sub_nodes

*(none yet)*

## settled

- **Implementation:** Cloned \`PseudoCoup_v3\` into \`Tools/PCv3.1\` and patched \`core.ledger\` and \`egress.cpp\` to correctly parse and respect ledger mappings (derived from PCHQ research concepts). This serves as our isolated working transpiler for the Chromium bindings swap!
