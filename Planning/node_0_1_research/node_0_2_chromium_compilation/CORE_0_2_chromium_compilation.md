---
id: ourobrowser.root.research.chromium_compilation
level: 2
status: draft
settled_by: Dee
supersedes: null
designation: pending
node:
    name: chromium_compilation
    path: Planning/node_0_1_research/node_0_2_chromium_compilation/CORE_0_2_chromium_compilation.md
super_node:
    name: research
    path: ../CORE_0_1_research.md
sub_nodes: []
---

# CORE 0_2 — chromium_compilation

## metadata

- **id:** ourobrowser.root.research.chromium_compilation
- **level:** 2
- **status:** draft
- **designation:** pending
- **settled_by:** Dee
- **supersedes:** null

## super_node

- [research](../CORE_0_1_research.md)

## sub_nodes

*(none yet)*

## definition

**Goal:** Modify the Chromium build system (GN/Ninja) to compile our PC-processed bindings.

**Details:**
- Chromium's build system expects to compile V8. We need to patch the `.gn` build files to exclude V8 compilation.
- Link the embedded Python runtime (e.g., `libpython3.so` or static equivalent) into the Chromium build.
- Ensure the newly PC-emitted binding files are added to the source lists in the `blink/renderer/bindings` `BUILD.gn` targets.
- The compiled artifact will be a fully functional web browser application that looks and behaves like Google Chrome, but whose DOM engine routes scripts strictly to Python.
