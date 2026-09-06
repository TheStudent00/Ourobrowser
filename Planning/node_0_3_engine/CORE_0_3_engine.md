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

- [browser_app](node_0_3_0_browser_app/CORE_0_3_0_browser_app.md)
- [scheme_handler](node_0_3_1_scheme_handler/CORE_0_3_1_scheme_handler.md) — `OurobrowserSchemeHandler` in `browser_engine.py`.
- [executor](node_0_3_2_executor/CORE_0_3_2_executor.md) — The one shared Python execution context, and the two ways code enters it.

## definition

The core `browser_engine.py` module. It sets up the QtWebEngine application, parses HTML to remove standard JS, extracts custom Python scripts, and executes them in a secure local environment.

## design

*(APPENDED 2026-09-03 by the task-77 implementer, on the instruction of
log_183 task 77. PROTOCOL §2 says a level-1 CORE changes only through
Dee, so this section is a ROLLUP of what the two sub-nodes below now
state, added so that a reader who stops here still has a correct
picture. Dee settles it; nothing here contradicts what stood before.)*

The engine gains a way for Python to put HTML on the page. Two
additions, at the two moments Python runs, plus one repair.

| addition | when it runs | where it is stated |
|---|---|---|
| `emit` — a python block puts HTML in its own place | request time, before Chromium sees the page | [scheme_handler](node_0_1_scheme_handler/CORE_0_1_scheme_handler.md) |
| `page_path` — a block knows the file it is in | request time | [scheme_handler](node_0_1_scheme_handler/CORE_0_1_scheme_handler.md) |
| `set_html` — python fills a named element | after first paint, on a click | [web_channel](../node_0_4_bridge/node_0_0_web_channel/CORE_0_0_web_channel.md) |
| the click wire form becomes an attribute, and the old inline rewrite is repaired | request time | [scheme_handler](node_0_1_scheme_handler/CORE_0_1_scheme_handler.md) |

- **Why two and not one.** A block runs before there is a DOM, so it
  cannot fill an element; a click runs after the block's text is gone,
  so it cannot fill a block. The two additions cover the two moments,
  and neither substitutes for the other. The reasoning is walked, with
  values in motion, in [executor](node_0_2_executor/CORE_0_2_executor.md).
- **Nothing that worked stops working.** A block that emits nothing is
  still replaced by the empty string; `execute_python` is unchanged;
  the JavaScript strip is unchanged.
