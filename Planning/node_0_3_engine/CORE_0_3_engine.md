---
id: ourobrowser.root.engine
level: 1
status: draft
settled_by: Dee
supersedes: null
designation: code (module)
node:
    name: engine
    path: Planning/node_0_3_engine/CORE_0_3_engine.md
super_node:
    name: Ourobrowser
    path: ../CORE_0.md
sub_nodes:
    - name: browser_app
      path: node_1_0_browser_app/CORE_1_0_browser_app.md
    - name: scheme_handler
      path: node_1_1_scheme_handler/CORE_1_1_scheme_handler.md
    - name: executor
      path: node_1_2_executor/CORE_1_2_executor.md
---

# CORE 0_3 — engine

## metadata

- **id:** ourobrowser.root.engine
- **level:** 1
- **status:** draft
- **designation:** code (module)
- **settled_by:** Dee
- **supersedes:** null

## super_node

- [Ourobrowser](../CORE_0.md)

## sub_nodes

- [browser_app](node_0_0_browser_app/CORE_0_0_browser_app.md)
- [scheme_handler](node_0_1_scheme_handler/CORE_0_1_scheme_handler.md)
- [executor](node_0_2_executor/CORE_0_2_executor.md)

## definition

The core `browser_engine.py` module. It sets up the QtWebEngine application, parses HTML to remove standard JS, extracts custom Python scripts, and executes them in a secure local environment.
