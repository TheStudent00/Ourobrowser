---
id: ourobrowser.root.progress
status: living
---

# PROGRESS — node_0

The living record of the whole tree. A sub-node's own PROGRESS carries the
detail; this file carries what changed about the PROJECT.

- 2026-09-03: the planning tree was generated from `CORE_0.md`'s register
  by `~/Programming/PlanPlan/framework/generate_nodes.py`, giving the six
  level-1 nodes: tools, research, api, engine, bridge, test_page. Status:
  **done**. Evidence: `git log --diff-filter=A -- Planning`.

- 2026-09-03: the PyQt6 engine gained `emit`, `page_path` and `set_html`,
  and the `onclick="python:…"` bridge — which had never reached python,
  because the rewrite served Chromium a page it refused — was repaired.
  Status: **done**. Evidence:
  `DevComms/log_001_python_renders_the_page.md`; the sub-node records are
  under [engine](node_0_3_engine/CORE_0_3_engine.md) and
  [bridge](node_0_4_bridge/CORE_0_4_bridge.md).

- 2026-09-04: Dee paused this line and began a second approach with
  Gemini — strip JavaScript out of QuteBrowser rather than build the
  interface from scratch. Status: **in-progress**. Evidence: the working
  copy at `Research/Qutebrowser_Fork`, three modified qutebrowser files
  and two new ones, none of them committed to that fork.

- 2026-09-04 to 2026-09-05: the [research](node_0_1_research/CORE_0_1_research.md)
  branch was opened and filled — a third approach, and the one the tree is
  mostly about: keep Chromium whole and use PseudoCoup to replace the
  Blink-to-V8 binding layer with a Blink-to-CPython one. Status:
  **in-progress**. Evidence: that node's PROGRESS.

- 2026-09-06: the tree was re-chained. Every folder below level 1 had
  restarted its numbering (`node_0_1_research/node_0_0_pc_ingress`)
  instead of carrying the address of the branch it sits on
  (`node_0_1_research/node_0_1_0_pc_ingress`), which PROTOCOL §1 requires
  and which the checker reads as a level-versus-depth disagreement. Healed
  by `~/Programming/PlanPlan/framework/heal_tree.py`, and every link
  repointed from what is on disk. Status: **done**. Evidence:
  `python3 ~/Programming/PlanPlan/framework/check_plans.py ~/Programming/Ourobrowser/Planning`
  went from 29 errors to 0; `DevComms/log_002_transpiler_keeps_the_source.md` §4.

- 2026-09-06: the transpiler stopped discarding the source it was given.
  A C++ construct PCv3.1 had no mapping for was dropped; seven Chromium
  headers had been rewritten in place down to their `#include` lines by
  that defect. The ingress now carries an unmapped construct through as
  its own text. Status: **done**. Evidence:
  `DevComms/log_002_transpiler_keeps_the_source.md`, and
  [pc_tools](node_0_1_research/node_0_1_3_pc_tools/CORE_0_1_3_pc_tools.md).

## the three approaches, and which node holds each

Three ways to reach one end — a browser whose pages are written in python
and which does not run JavaScript. They are not stages of one plan; each
could be the answer on its own, and each has its own node.

| approach | what it is | node |
|---|---|---|
| the PyQt6 engine | a browser this project writes, serving its own pages through the `ourobrowser://` scheme | [engine](node_0_3_engine/CORE_0_3_engine.md), [bridge](node_0_4_bridge/CORE_0_4_bridge.md) |
| the QuteBrowser fork | the same scheme handler and bridge installed into an existing PyQt6 browser | *(no node yet — the working copy is `Research/Qutebrowser_Fork`)* |
| the Chromium swap | Chromium kept whole, its Blink-to-V8 bindings replaced by Blink-to-CPython bindings the transpiler emits | [research](node_0_1_research/CORE_0_1_research.md) |
