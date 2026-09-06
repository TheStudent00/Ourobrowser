---
id: ourobrowser.root.research.api_mapping.trickle_injection.ledger_writer
level: 4
status: settled
settled_by: Dee
supersedes: null
designation: code (patch)
node:
    name: ledger_writer
    path: Planning/node_0_1_research/node_0_7_api_mapping/node_0_2_trickle_injection/node_0_1_ledger_writer/CORE_0_1_ledger_writer.md
super_node:
    name: trickle_injection
    path: ../CORE_0_2_trickle_injection.md
sub_nodes: []
---

# CORE 0_1 — ledger_writer

## metadata

- **id:** ourobrowser.root.research.api_mapping.trickle_injection.ledger_writer
- **level:** 4
- **status:** draft
- **designation:** code (patch)
- **settled_by:** Dee
- **supersedes:** null

## super_node

- [trickle_injection](../CORE_0_2_trickle_injection.md)

## sub_nodes

*(none)*

## definition

Patch `transpiler_loop.py` to seamlessly bake the `GLOBAL_FUNCTIONS` into the dynamically generated `.ledger.json`.
