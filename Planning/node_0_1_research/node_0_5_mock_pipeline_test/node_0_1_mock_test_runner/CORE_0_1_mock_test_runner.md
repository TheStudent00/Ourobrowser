---
id: ourobrowser.root.research.mock_pipeline_test.mock_test_runner
level: 1
status: settled
settled_by: Dee
supersedes: null
designation: code (module)
node:
    name: mock_test_runner
    path: node_0_5_mock_pipeline_test/node_0_1_mock_test_runner/CORE_0_1_mock_test_runner.md
super_node:
    name: mock_pipeline_test
    path: ../CORE_0_5_mock_pipeline_test.md
sub_nodes: []
---

# CORE 0_1 — mock_test_runner

## metadata

- **id:** ourobrowser.root.research.mock_pipeline_test.mock_test_runner
- **level:** 1
- **status:** settled
- **designation:** code (module)
- **settled_by:** Dee
- **supersedes:** null

## super_node

- [mock_pipeline_test](../CORE_0_5_mock_pipeline_test.md)

## sub_nodes

*(none yet)*

## definition

*(pending — generated 2026-09-04 from the register in
~/Programming/Ourobrowser/Planning/node_0_1_research/node_0_5_mock_pipeline_test/CORE_0_5_mock_pipeline_test.md; the definition and `designation` are Dee's to
write.)*

## settled

- **Implementation:** Created `mock_test_runner.sh` to run the ingress and egress phases on the isolated mock file.

- **Blocker:** `mock_test_runner.sh` fails because `~/Programming/PseudoIR/pseudoir/emit` is empty on disk, preventing PseudoCoup from importing `get_emitter`.

- **Resolved:** Switched to `PseudoCoup_v3` because v4 was broken due to missing `PseudoIR` dependencies. The mock pipeline ran successfully with PCv3, though the `CppEmitter` in v3 requires upgrading to fully respect the Ledger type maps before applying to the full Chromium codebase.
