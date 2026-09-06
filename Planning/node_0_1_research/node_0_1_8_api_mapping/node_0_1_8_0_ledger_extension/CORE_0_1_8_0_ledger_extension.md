---
id: ourobrowser.root.research.api_mapping.ledger_extension
level: 3
status: settled
settled_by: Dee
supersedes: null
designation: code (module)
node:
    name: ledger_extension
    path: Planning/node_0_1_research/node_0_1_8_api_mapping/node_0_1_8_0_ledger_extension/CORE_0_1_8_0_ledger_extension.md
super_node:
    name: api_mapping
    path: ../CORE_0_7_api_mapping.md
sub_nodes:
    - name: schema_update
      path: node_0_0_schema_update/CORE_0_0_schema_update.md
    - name: resolve_method
      path: node_0_1_resolve_method/CORE_0_1_resolve_method.md
---

# CORE 0_1_8_0 — ledger_extension

## metadata

- **id:** ourobrowser.root.research.api_mapping.ledger_extension
- **level:** 3
- **status:** settled
- **designation:** code (module)
- **settled_by:** Dee
- **supersedes:** null

## super_node

- [api_mapping](../CORE_0_7_api_mapping.md)

## sub_nodes

- [schema_update](node_0_1_8_0_0_schema_update/CORE_0_1_8_0_0_schema_update.md) — Update the Ledger initialization to accept the 'functions' mapping schema block.
- [resolve_method](node_0_1_8_0_1_resolve_method/CORE_0_1_8_0_1_resolve_method.md) — Implement the `resolve_function(fqdn)` logic to query the function mapping dictionary.

## definition

Extend the PCv3.1 Ledger in `pseudocoup/core/ledger.py` to ingest a `"functions"` block and provide a `resolve_function(fqdn)` method.
