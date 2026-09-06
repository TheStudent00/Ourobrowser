---
id: ourobrowser.root.engine.executor
level: 1
status: draft
settled_by: Dee
supersedes: null
designation: pending
node:
    name: executor
    path: node_0_3_engine/node_0_2_executor/CORE_0_2_executor.md
super_node:
    name: engine
    path: ../CORE_0_3_engine.md
sub_nodes: []
---

# CORE 0_2 — executor

## metadata

*(pending)*

## super_node

- [engine](../CORE_0_3_engine.md)

## sub_nodes

*(none yet)*

## definition

The one shared Python execution context, and the two ways code enters
it. A page's `<script type="text/python">` blocks enter it at REQUEST
time, before Chromium has seen any HTML. A click's expression enters
it later, through the bridge, while the page is on screen. Both `exec`
into the same dictionary, so a function a block defined is callable by
a click.

*(This paragraph describes code that already runs; it was written
2026-09-03 by the task-77 implementer so that the design below has a
definition to sit under. The node's `designation` is still Dee's.)*

## design

*(added 2026-09-03 by the task-77 implementer. Provenance: log_183
task 77. Working names; Dee settles them.)*

- **The context is one dictionary, `OurobrowserWindow.python_context`,
  passed to both the scheme handler and the bridge.** Unchanged.
- **A block runs BEFORE the DOM exists; a click runs AFTER it.** That
  is the whole reason two additions are needed rather than one:
  - at request time there is no element to push HTML into, so a block
    puts its HTML in its own place — `emit`, defined in the
    scheme_handler node;
  - at click time the block's text is long gone, so the only way to
    change the page is to push into an element that is already there —
    `set_html`, defined in the bridge node.
- **Both names are bound in the same context, so a page reads as one
  program.** A block calls `emit` for the first paint and defines the
  functions the buttons call; those functions call `set_html`. Values
  in motion, on the dashboard page this was built for:

```
request time
	block runs
		defines ouro_pane(n)
		calls emit("<div id=pane>…pane 5…</div>")
	handler substitutes that html for the block
	handler rewrites onclick="python:ouro_pane(2)"
		to data-python-onclick="ouro_pane(2)"
Chromium paints

click on the pane-2 button
	setup script reads the attribute
	bridge exec's "ouro_pane(2)" in the same context
	ouro_pane builds pane 2's html in python
	ouro_pane calls set_html("pane", html)
	bridge emits html_pushed("pane", html)
	setup script sets that element's innerHTML
```

- **A block's exception is printed and the page still loads.** The
  existing behaviour, unchanged: a failed block leaves the page
  standing rather than failing the request.

## settled rules

*(added 2026-09-03 by the task-77 implementer; each carries its
decision source.)*

- **One context, two entry times, never two contexts.** Decision: the
  code as it already stands — `~/Programming/Ourobrowser/browser_engine.py`
  builds `self.python_context = {}` once and hands the same object to
  `PythonBridge` and to `OurobrowserSchemeHandler`.
- **A name the engine binds into the context is bound at the moment it
  can work, and not before.** `emit` exists only while a block is
  running, because after that there is no block for it to fill.
  Decision: this CORE, 2026-09-03.
