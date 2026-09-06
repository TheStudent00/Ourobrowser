---
id: ourobrowser.root.research.api_mapping.trickle_injection
level: 3
status: settled
settled_by: Dee
supersedes: null
designation: code (module)
node:
    name: trickle_injection
    path: Planning/node_0_1_research/node_0_1_8_api_mapping/node_0_1_8_2_trickle_injection/CORE_0_1_8_2_trickle_injection.md
super_node:
    name: api_mapping
    path: ../CORE_0_1_8_api_mapping.md
sub_nodes:
    - name: mapping_dictionary
      path: node_0_1_8_2_0_mapping_dictionary/CORE_0_1_8_2_0_mapping_dictionary.md
    - name: ledger_writer
      path: node_0_1_8_2_1_ledger_writer/CORE_0_1_8_2_1_ledger_writer.md
---

# CORE 0_1_8_2 — trickle_injection

## metadata

- **id:** ourobrowser.root.research.api_mapping.trickle_injection
- **level:** 3
- **status:** settled
- **designation:** code (module)
- **settled_by:** Dee
- **supersedes:** null

## super_node

- [api_mapping](../CORE_0_1_8_api_mapping.md)

## sub_nodes

- [mapping_dictionary](node_0_1_8_2_0_mapping_dictionary/CORE_0_1_8_2_0_mapping_dictionary.md) — Create the `GLOBAL_FUNCTIONS` constant dictionary holding all known V8 to CPython C-API mappings.
- [ledger_writer](node_0_1_8_2_1_ledger_writer/CORE_0_1_8_2_1_ledger_writer.md) — Patch `transpiler_loop.py` to seamlessly bake the `GLOBAL_FUNCTIONS` into the dynamically generated `.ledger.json`.

## definition

Update `transpiler_loop.py` to inject the `GLOBAL_FUNCTIONS` dict containing known V8 to CPython mappings directly into the generated `.ledger.json`.
