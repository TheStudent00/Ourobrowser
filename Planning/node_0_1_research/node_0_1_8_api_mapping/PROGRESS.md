# PROGRESS 0_7 — api_mapping

- [x] **done** — Extend PCv3.1 Ledger to support `"functions"` schema.
- [x] **done** — Modify `CppEmitter.visit_CallNode` to execute function swapping via the Ledger format strings.
- [x] **done** — Update `transpiler_loop.py` to write the global function mapping dictionary into the `.ledger.json` on each iteration.
- [x] **done** — Let the `trickle_loop.sh` run and manually review the generated transpiled C++ output on `v8_string_demo.cc` or a live Chromium file.

- 2026-09-06: the ledger gained a second form of function key. A key
  beginning with `.` names a METHOD by name alone, and `{self}` in its
  value stands for whatever the method was called on, so
  `".ToLocalChecked": "{self}"` unwraps a `v8::MaybeLocal` to the value
  inside it. Status: **done**. Evidence:
  `~/Programming/Ourobrowser/DevComms/log_002_transpiler_keeps_the_source.md`
  §4, where `v8::String::NewFromUtf8(isolate, str).ToLocalChecked()`
  becomes `PyUnicode_FromString(str)`.

- 2026-09-06: type mapping now reaches a written type. A ledger key of
  the form `.<type as written>` is consulted for every declaration, so
  `.v8::Isolate*` maps a parameter declared `v8::Isolate* isolate` to
  `PyInterpreterState* isolate`. Before this the emitter read only the
  `type` field of the parse, which drops the `*`, so `const char* str`
  became `char str`. Status: **done**. Evidence: log_002 §3.4.
