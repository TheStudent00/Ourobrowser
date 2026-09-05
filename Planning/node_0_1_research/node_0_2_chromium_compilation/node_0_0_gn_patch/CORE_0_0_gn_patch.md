---
id: ourobrowser.root.research.chromium_compilation.gn_patch
level: 1
status: settled
settled_by: Dee
supersedes: null
designation: code (patch)
decision: node_0_0_gn_patch/CORE_0_0_gn_patch.md#settled
node:
    name: gn_patch
    path: node_0_2_chromium_compilation/node_0_0_gn_patch/CORE_0_0_gn_patch.md
super_node:
    name: chromium_compilation
    path: ../CORE_0_2_chromium_compilation.md
sub_nodes: []
---

# CORE 0_0 — gn_patch

## metadata

**Goal:** Write build_v8_to_python.patch

**Details:**
Draft the unified diff modifying Chromium's `BUILD.gn` to remove `//v8` dependencies and inject `//build/config/python:embed`.

## super_node

*(none)*

## sub_nodes

*(none — leaf node)*

## definition

*(pending — generated 2026-09-04 from the register in
~/Programming/Ourobrowser/Planning/node_0_1_research/node_0_2_chromium_compilation/CORE_0_2_chromium_compilation.md; the definition and `designation` are Dee's to
write.)*

## settled

- **Implementation:** Created `Research/chromium_compilation/build_v8_to_python.patch` to remove V8.
