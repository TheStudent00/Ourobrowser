---
id: ourobrowser.root.research.runtime_embedding
level: 2
status: draft
settled_by: Dee
supersedes: null
designation: pending
node:
    name: runtime_embedding
    path: Planning/node_0_1_research/node_0_3_runtime_embedding/CORE_0_3_runtime_embedding.md
super_node:
    name: research
    path: ../CORE_0_1_research.md
sub_nodes: []
---

# CORE 0_3 — runtime_embedding

## metadata

- **id:** ourobrowser.root.research.runtime_embedding
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

**Goal:** Establish and manage the local embedded Python runtime natively inside the compiled Chromium processes.

**Details:**
- Because the PCHQ Hub is currently theoretical, the translated browser must execute its logic locally, exactly like the original V8 engine did.
- Chromium's architecture typically spins up isolated V8 environments (Isolates) for each tab/renderer process. We must replicate this by injecting `Py_Initialize()` into Chromium's renderer process initialization logic.
- We must establish a sandboxed local Python context (`dict`) for each frame so that `<script type="text/python">` execution spaces do not cross-contaminate between different websites or tabs.
- Ensure the Python Global Interpreter Lock (GIL) is managed gracefully so that Chromium's multi-threaded rendering pipeline (Blink) remains completely non-blocking while Python handles DOM events.
- The end result is a standalone, fully-functional browser that runs Python natively via embedded CPython, with no external dependencies required.
