---
id: ourobrowser.root.bridge.web_channel
level: 2
status: draft
settled_by: Dee
supersedes: null
designation: pending
node:
    name: web_channel
    path: Planning/node_0_4_bridge/node_0_4_0_web_channel/CORE_0_4_0_web_channel.md
super_node:
    name: bridge
    path: ../CORE_0_4_bridge.md
sub_nodes: []
nodes: []
---

# CORE 0_4_0 — web_channel

## metadata

*(pending)*

## super_node

- [bridge](../CORE_0_4_bridge.md)

## sub_nodes

*(none yet)*

## definition

The `QWebChannel` wiring: `PythonBridge` is registered on the channel
under the name `pyBridge`, the page's setup script builds the matching
`QWebChannel` object, and the two ends talk. Today the traffic runs one
way — the page calls `PythonBridge.execute_python`, whose return value
is discarded.

*(This paragraph describes code that already runs; it was written
2026-09-03 by the task-77 implementer so that the design below has a
definition to sit under. The node's `designation` is still Dee's.)*

## design

*(added 2026-09-03 by the task-77 implementer. Provenance: log_183
task 77 —* "there is no path from Python back into the DOM … the bridge
cannot answer" *. Working names; Dee settles them.)*

```
class PythonBridge
	attributes:
		context
		rewriter
	signals:
		html_pushed(str, str)
	methods:
		execute_python
		set_html
```

- **ADDITION — a Qt signal is the return path.** `html_pushed` carries
  two strings: the `id` of the element to fill, and the HTML to put in
  it. QWebChannel already publishes a registered object's signals to
  the page, so the setup script subscribes to it in one line and no new
  transport is invented.
- **`set_html(target, html)` is what Python calls.** It runs the
  engine's click rewrite over the html and then emits `html_pushed`. It
  is a method rather than a bare `emit` so that the rewrite can never
  be forgotten by a caller.
- **The rewrite is INJECTED, not imported.** `PythonBridge.__init__`
  takes a `rewriter` callable and defaults it to the identity. The
  engine passes its own `rewrite_python_onclick` when it builds the
  bridge. The bridge therefore never imports the engine, and the
  engine's existing import of the bridge stays one-directional.
- **Nothing about `execute_python` changes.** It still `exec`s in the
  shared context and still discards the return value. The answer comes
  back as a signal instead, which is why the discarded return value
  never had to become a returned one.
- **Values in motion.** `set_html("pane", "<b onclick=\"python:go()\">x</b>")`
  runs the rewrite, producing
  `<b data-python-onclick="go()">x</b>`, emits
  `html_pushed("pane", that string)`, and the setup script assigns it
  to `document.getElementById("pane").innerHTML`. The delegated click
  listener is on `document`, so the element that has just arrived is
  already live — nothing re-wires it.

## settled rules

*(added 2026-09-03 by the task-77 implementer; each carries its
decision source.)*

- **The bridge answers with a signal, never with a return value.**
  Decision: this CORE, 2026-09-03. Reason recorded: QWebChannel
  delivers a slot's return value only to an asynchronous callback in
  the page, which would put page-authored JavaScript back into the
  design the project exists to remove.
- **HTML that Python pushes is rewritten by the same function the
  scheme handler uses.** One implementation, two callers. Decision:
  this CORE, 2026-09-03.
- **The bridge does not import the engine.** The rewrite arrives as a
  constructor argument. Decision: this CORE, 2026-09-03; the engine
  already imports the bridge, so the other direction would be a cycle.

## members

The code members of this node, in `bridge.py`, class PythonBridge. Each is a member of one
file, not a planning node: a planning node is a folder carrying its
own CORE, and none of these has one. They were written into the
`sub_nodes` edge register, which the framework reads as edges to node
folders; moved here 2026-09-06 so the register states only edges.

- `execute_python` — code (method)
- `set_html` — code (method)
