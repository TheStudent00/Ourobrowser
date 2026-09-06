---
id: ourobrowser.root.engine.scheme_handler
level: 2
status: draft
settled_by: Dee
supersedes: null
designation: pending
node:
    name: scheme_handler
    path: Planning/node_0_3_engine/node_0_3_1_scheme_handler/CORE_0_3_1_scheme_handler.md
super_node:
    name: engine
    path: ../CORE_0_3_engine.md
sub_nodes: []
nodes: []
---

# CORE 0_3_1 — scheme_handler

## metadata

*(pending)*

## super_node

- [engine](../CORE_0_3_engine.md)

## sub_nodes

*(none yet)*

## definition

`OurobrowserSchemeHandler` in `browser_engine.py`. It answers every
`ourobrowser://local/<path>` request: it opens the file named by the
path, executes the page's `<script type="text/python">` blocks in the
shared context, strips every other `<script>`, rewrites the page's
`python:` click handlers into the bridge's wire form, appends the
engine's own setup script, and replies with the result.

*(This paragraph describes code that already runs; it was written
2026-09-03 by the task-77 implementer so that the design below has a
definition to sit under. The node's `designation` is still Dee's.)*

## design

*(added 2026-09-03 by the task-77 implementer. Provenance: log_183
task 77, which quotes Dee's own request —* "the browser allows python
to be run locally natively within the browser. id like to see the
dashboard written to run in it" *— and states the gap it runs into:*
"there is no path from Python back into the DOM. A
`<script type="text/python">` cannot emit HTML (its text is replaced
by the empty string) and the bridge cannot answer." *Every name below
is a WORKING name, each defined in exactly one place, and every one of
them is Dee's to change.)*

Three additions and one repair. Each is stated as what the handler
does, in the order the handler already does it.

```
class OurobrowserSchemeHandler
	attributes:
		context
	methods:
		requestStarted
	module names it owns, one definition each:
		PAGE_EMIT_NAME        "emit"
		PAGE_PATH_NAME        "page_path"
		PYTHON_CLICK_ATTRIBUTE
		                      "data-python-onclick"
	module functions:
		rewrite_python_onclick
```

- **ADDITION 1 — a python block may emit HTML in place of itself.**
  Before a block is executed the handler binds one name in the shared
  context, `PAGE_EMIT_NAME`, to a collector. The block calls it as
  many times as it likes; the concatenation of what it collected
  replaces the block's own text in the HTML Chromium receives. A block
  that never calls it is replaced by the empty string, exactly as
  before, so every page written against the old behaviour is
  unaffected.
- **ADDITION 2 — a block knows which file it is in.** Before a block
  is executed the handler binds `PAGE_PATH_NAME` in the shared context
  to the absolute path of the file being served. Without it a page
  cannot reach anything that sits beside it, and the page would have
  to carry a machine-specific path in its own text.
- **ADDITION 3 — the click handler's wire form is an attribute, not
  inline code.** `onclick="python:EXPR"` is rewritten to
  `PYTHON_CLICK_ATTRIBUTE="EXPR"`, with `EXPR` html-escaped. Nothing
  executable is written into the page. The engine's own setup script
  carries ONE delegated click listener that reads the attribute and
  hands the expression to the bridge.
- **THE REPAIR — the old rewrite emitted a page that could not run.**
  The replacement template `...execute_python(\'\1\')...` was a raw
  python string, so the backslashes reached Chromium literally. See
  the settled rule below for the literal and the browser's own error.
- **The rewrite is one function, `rewrite_python_onclick`, and the
  bridge uses the same one.** HTML that Python pushes into the page
  after first paint never passes through `requestStarted`, so it would
  otherwise carry `python:` handlers nothing had rewritten. The engine
  hands the function to the bridge when it builds it; the bridge does
  not import the engine.
- **Order is unchanged and load-bearing.** Blocks are executed and
  replaced first, other scripts are stripped second, the click rewrite
  runs third, the setup script is appended fourth. Because the rewrite
  runs after the emission, HTML a block emits gets its `python:`
  handlers rewritten like any other; because the strip runs before it,
  emitted HTML cannot smuggle JavaScript in.

## settled rules

*(added 2026-09-03 by the task-77 implementer; each carries its
decision source, per PROTOCOL §5.)*

- **A block that emits nothing behaves exactly as it did.** The
  substitution is the empty string when the collector is empty.
  Decision: this CORE, 2026-09-03, from log_183 task 77's requirement
  "Keep `test_page.html` working".
- **No executable text is written into a page by the engine except its
  own setup script.** The click wire form is an attribute; the
  listener lives in the setup script. Decision: this CORE, 2026-09-03,
  extending the project's own stated feature — README.md,
  `~/Programming/Ourobrowser/README.md`: "Standard `<script>` tags are
  completely stripped and ignored."
- **The old inline rewrite was broken, measured, not asserted.** The
  literal the old code served to Chromium, printed by running the same
  regular expression over `~/Programming/Ourobrowser/test_page.html`:

  ```
  <button onclick="if(window.pyBridge) { window.pyBridge.execute_python(\'fetch_system_data()\'); }">Fetch System Data (Python)</button>
  ```

  and Chromium's own answer when that button is clicked:

  ```
  js: Uncaught SyntaxError: Failed to execute 'click' on 'HTMLElement': Invalid or unexpected token
  ```

  So the bridge never fired from a page. Decision: this CORE,
  2026-09-03; evidence class **forced by construction** (the served
  text and the browser's refusal of it).
- **Every name introduced here is provisional and lives in one
  place.** `PAGE_EMIT_NAME`, `PAGE_PATH_NAME` and
  `PYTHON_CLICK_ATTRIBUTE` are module-level names in
  `browser_engine.py`; changing a name is one edit. Decision:
  log_183's standing rule that architecture, ontology and naming are
  Dee's.

## members

The code members of this node, in `browser_engine.py`, class OurobrowserSchemeHandler. Each is a member of one
file, not a planning node: a planning node is a folder carrying its
own CORE, and none of these has one. They were written into the
`sub_nodes` edge register, which the framework reads as edges to node
folders; moved here 2026-09-06 so the register states only edges.

- `requestStarted` — code (method)
- `rewrite_python_onclick` — code (function)
- `PAGE_EMIT_NAME` — code (constant)
