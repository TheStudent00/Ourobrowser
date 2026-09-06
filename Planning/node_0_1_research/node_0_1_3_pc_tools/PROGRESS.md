---
id: ourobrowser.root.research.pc_tools.progress
status: living
---

# PROGRESS — pc_tools

- 2026-09-05: `PseudoCoup_v3` cloned into `Tools/PCv3.1`. Status:
  **done**. Evidence: `Tools/PCv3.1/`, whose git remote is
  `https://github.com/TheStudent00/PseudoCoup_v3.git`.

- 2026-09-05: the ledger gained a `functions` block and
  `resolve_function`, and `CppEmitter.visit_CallNode` began consulting it,
  so a V8 call can be swapped for a Python C-API call. Status: **done**.
  Evidence: [api_mapping](../node_0_1_8_api_mapping/CORE_0_1_8_api_mapping.md).

- 2026-09-06: the node arrived carrying no `id`, no `level`, no PROGRESS
  and no CHECK, so nothing above it could be answered; all four written.
  Status: **done**. Evidence: this file, and
  `python3 ~/Programming/PlanPlan/framework/check_plans.py ~/Programming/Ourobrowser/Planning`.

- 2026-09-06: the C++ ingress and the C++ emitter were rewritten so a C++
  source survives a round trip. Status: **done**. Evidence:
  `DevComms/log_002_transpiler_keeps_the_source.md`.
