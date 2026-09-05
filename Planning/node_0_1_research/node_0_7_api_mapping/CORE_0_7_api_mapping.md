---
id: ourobrowser.root.research.api_mapping
level: 2
status: draft
settled_by: Dee
supersedes: null
designation: work
node:
    name: api_mapping
    path: Planning/node_0_1_research/node_0_7_api_mapping/CORE_0_7_api_mapping.md
super_node:
    name: research
    path: ../CORE_0_1_research.md
sub_nodes: []
---

# CORE 0_7 — api_mapping

## metadata

- **id:** ourobrowser.root.research.api_mapping
- **level:** 2
- **status:** draft
- **designation:** work
- **settled_by:** Dee
- **supersedes:** null

## super_node

- [research](../CORE_0_1_research.md)

## sub_nodes

*(none)*

## definition

Extend `PCv3.1` to support API function call mappings (modeled after PCHQ's `op_pipeline` manifest). The transpiler must swap underlying function calls like `v8::String::NewFromUtf8` with `PyUnicode_FromString` and restructure arguments as necessary.
