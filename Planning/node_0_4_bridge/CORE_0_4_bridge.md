---
id: pybrowser.root.bridge
level: 1
status: draft
settled_by: Dee
supersedes: null
designation: code (module)
node:
    name: bridge
    path: Planning/node_0_4_bridge/CORE_0_4_bridge.md
super_node:
    name: PyBrowser
    path: ../CORE_0.md
sub_nodes:
    - name: web_channel
      path: node_1_0_web_channel/CORE_1_0_web_channel.md
---

# CORE 0_4 — bridge

## metadata

- **id:** pybrowser.root.bridge
- **level:** 1
- **status:** draft
- **designation:** code (module)
- **settled_by:** Dee
- **supersedes:** null

## super_node

- [PyBrowser](../CORE_0.md)

## sub_nodes

- [web_channel](node_0_0_web_channel/CORE_0_0_web_channel.md)

## definition

The `bridge.py` module establishes the bidirectional communication channel between the DOM and the Python backend using QWebChannel. It exposes Python objects to the web engine and forwards UI events to the native Python execution context.
