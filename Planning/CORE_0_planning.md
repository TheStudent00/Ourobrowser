---
id: ourobrowser.root
level: 0
status: draft
settled_by: Dee
supersedes: null
designation: work
node:
    name: Ourobrowser
    path: Planning/CORE_0_planning.md
    repo: Ourobrowser
    remote: https://github.com/TheStudent00/Ourobrowser.git
super_node: null
sub_nodes:
    - name: tools
      path: node_0_0_tools/CORE_0_0_tools.md
    - name: research
      path: node_0_1_research/CORE_0_1_research.md
    - name: api
      path: node_0_2_api/CORE_0_2_api.md
    - name: engine
      path: node_0_3_engine/CORE_0_3_engine.md
    - name: bridge
      path: node_0_4_bridge/CORE_0_4_bridge.md
    - name: test_page
      path: node_0_5_test_page/CORE_0_5_test_page.md
---

# CORE 0 — planning

## metadata

- **id:** ourobrowser.root
- **level:** 0
- **status:** draft
- **designation:** work
- **settled_by:** Dee
- **supersedes:** null

## super_node

*(none — tree root)*

## sub_nodes

- [tools](node_0_0_tools/CORE_0_0_tools.md)
- [research](node_0_1_research/CORE_0_1_research.md) — This branch represents the physically separate research and execution plan for using PseudoCoup (PC) to systematically swap the V8 JavaScript engine for a local, embedded Python execution engine inside the Chromium C++ codebase.
- [api](node_0_2_api/CORE_0_2_api.md)
- [engine](node_0_3_engine/CORE_0_3_engine.md) — The core `browser_engine.py` module.
- [bridge](node_0_4_bridge/CORE_0_4_bridge.md) — The `bridge.py` module establishes the bidirectional communication channel between the DOM and the Python backend using QWebChannel.
- [test_page](node_0_5_test_page/CORE_0_5_test_page.md) — The `test_page.html` file acts as the primary demonstration for the Ourobrowser.

## definition

Ourobrowser is a prototype browser wrapper using PyQt6 that natively parses HTML/CSS but intercepts and completely replaces standard JavaScript execution with a custom Python execution engine. It includes bidirectional DOM-to-Python bridging.
