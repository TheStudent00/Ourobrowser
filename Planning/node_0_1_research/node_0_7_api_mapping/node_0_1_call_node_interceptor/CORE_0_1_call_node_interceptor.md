---
id: ourobrowser.root.research.api_mapping.call_node_interceptor
level: 3
status: draft
settled_by: Dee
supersedes: null
designation: code (module)
node:
    name: call_node_interceptor
    path: Planning/node_0_1_research/node_0_7_api_mapping/node_0_1_call_node_interceptor/CORE_0_1_call_node_interceptor.md
super_node:
    name: api_mapping
    path: ../CORE_0_7_api_mapping.md
sub_nodes: []
---

# CORE 0_7_1 — call_node_interceptor

## metadata

- **id:** ourobrowser.root.research.api_mapping.call_node_interceptor
- **level:** 3
- **status:** draft
- **designation:** code (module)
- **settled_by:** Dee
- **supersedes:** null

## super_node

- [api_mapping](../CORE_0_7_api_mapping.md)

## sub_nodes

*(none)*

## definition

Modify `CppEmitter.visit_CallNode` in `pseudocoup/egress/cpp.py` to flatten `node.func_name` to an FQDN, resolve it via the Ledger, and restructure arguments using format strings.
