---
id: pybrowser.root
level: 0
status: draft
settled_by: Dee
supersedes: null
designation: work
node:
    name: PyBrowser
    path: Planning/CORE_0.md
    repo: PyBrowser
    remote: https://github.com/TheStudent00/PyBrowser.git
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

# CORE 0 — PyBrowser

## metadata

- **id:** pybrowser.root
- **level:** 0
- **status:** draft
- **designation:** work
- **settled_by:** Dee
- **supersedes:** null

## super_node

*(none — tree root)*

## sub_nodes

- [tools](node_0_0_tools/CORE_0_0_tools.md)
- [research](node_0_1_research/CORE_0_1_research.md)
- [api](node_0_2_api/CORE_0_2_api.md)
- [engine](node_0_3_engine/CORE_0_3_engine.md)
- [bridge](node_0_4_bridge/CORE_0_4_bridge.md)
- [test_page](node_0_5_test_page/CORE_0_5_test_page.md)

## definition

PyBrowser is a prototype browser wrapper using PyQt6 that natively parses HTML/CSS but intercepts and completely replaces standard JavaScript execution with a custom Python execution engine. It includes bidirectional DOM-to-Python bridging.
