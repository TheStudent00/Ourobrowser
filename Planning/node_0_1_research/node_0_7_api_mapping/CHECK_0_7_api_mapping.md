# CHECK 0_7 — api_mapping

- [ ] Does PCv3.1 Ledger properly ingest `"functions"` mappings with parameter format strings (e.g. `PyUnicode_FromString({1})`)?
- [ ] Does `CppEmitter.visit_CallNode` accurately flatten attribute chains to correctly lookup FQDN function calls?
- [ ] Does the `trickle_loop.sh` dynamically generate the `.ledger.json` with `GLOBAL_FUNCTIONS` mappings included?
