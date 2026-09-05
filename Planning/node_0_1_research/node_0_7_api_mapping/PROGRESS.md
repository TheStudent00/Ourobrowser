# PROGRESS 0_7 — api_mapping

- [x] **done** — Extend PCv3.1 Ledger to support `"functions"` schema.
- [x] **done** — Modify `CppEmitter.visit_CallNode` to execute function swapping via the Ledger format strings.
- [x] **done** — Update `transpiler_loop.py` to write the global function mapping dictionary into the `.ledger.json` on each iteration.
- [x] **done** — Let the `trickle_loop.sh` run and manually review the generated transpiled C++ output on `v8_string_demo.cc` or a live Chromium file.
