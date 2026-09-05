---
id: ourobrowser.root.research.api_mapping.trickle_injection
level: 3
status: draft
settled_by: Dee
supersedes: null
designation: code (module)
node:
    name: trickle_injection
    path: Planning/node_0_1_research/node_0_7_api_mapping/node_0_2_trickle_injection/CORE_0_2_trickle_injection.md
super_node:
    name: api_mapping
    path: ../CORE_0_7_api_mapping.md
sub_nodes: []
---

# CORE 0_7_2 — trickle_injection

## metadata

- **id:** ourobrowser.root.research.api_mapping.trickle_injection
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

Update `transpiler_loop.py` to inject the `GLOBAL_FUNCTIONS` dict containing known V8 to CPython mappings directly into the generated `.ledger.json`.
