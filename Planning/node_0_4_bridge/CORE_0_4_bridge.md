---
id: ourobrowser.root.bridge
level: 1
status: draft
settled_by: Dee
supersedes: null
designation: code (module)
node:
    name: bridge
    path: Planning/node_0_4_bridge/CORE_0_4_bridge.md
super_node:
    name: Ourobrowser
    path: ../CORE_0.md
sub_nodes:
    - name: web_channel
      path: node_1_0_web_channel/CORE_1_0_web_channel.md
---

# CORE 0_4 — bridge

## metadata

- **id:** ourobrowser.root.bridge
- **level:** 1
- **status:** draft
- **designation:** code (module)
- **settled_by:** Dee
- **supersedes:** null

## super_node

- [Ourobrowser](../CORE_0.md)

## sub_nodes

- [web_channel](node_0_0_web_channel/CORE_0_0_web_channel.md)

## definition

The `bridge.py` module establishes the bidirectional communication channel between the DOM and the Python backend using QWebChannel. It exposes Python objects to the web engine and forwards UI events to the native Python execution context.

## design

*(APPENDED 2026-09-03 by the task-77 implementer, on the instruction of
log_183 task 77. PROTOCOL §2 says a level-1 CORE changes only through
Dee, so this section is a ROLLUP of what the sub-node below now states.
Dee settles it.)*

The definition above says the channel is "bidirectional". It was not:
the page could call Python and Python could not answer, and the click
rewrite that was supposed to carry the one direction that existed
emitted a page Chromium refused to run.

- **`PythonBridge.html_pushed`** — a Qt signal carrying an element id
  and a string of HTML. QWebChannel already publishes a registered
  object's signals, so this is the return path with no new transport.
- **`PythonBridge.set_html(target, html)`** — what Python calls. It
  runs the engine's click rewrite over the html, then emits the signal.
- **`PythonBridge(context=…, rewriter=…)`** — the rewrite is injected
  by the engine, so the bridge never imports the engine.

Stated in full, with the values moving through it, in
[web_channel](node_0_0_web_channel/CORE_0_0_web_channel.md).
