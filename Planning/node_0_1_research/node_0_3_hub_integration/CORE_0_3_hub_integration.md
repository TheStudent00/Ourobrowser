---
id: ourobrowser.root.research.hub_integration
level: 2
status: draft
settled_by: Dee
supersedes: null
designation: pending
node:
    name: hub_integration
    path: Planning/node_0_1_research/node_0_3_hub_integration/CORE_0_3_hub_integration.md
super_node:
    name: research
    path: ../CORE_0_1_research.md
sub_nodes: []
---

# CORE 0_3 — hub_integration

## metadata

- **id:** ourobrowser.root.research.hub_integration
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

**Goal:** Bridge the embedded Python DOM environment into the external PCHQ Hub.

**Details:**
- The new Chromium fork now natively runs `<script type="text/python">`. 
- However, we want this local Python runtime to act as a dumb relay to the broader PCHQ Hub, allowing multi-language processing.
- We will inject an IPC mechanism (such as local WebSockets or a shared memory queue) into the embedded Python environment.
- When an `onclick` DOM event fires in the browser, it is caught natively by the new Python bindings, and then relayed directly to the PCHQ Hub for evaluation.
- The PCHQ Hub computes the result (in whatever language) and streams DOM mutations back to the browser's Python execution layer, which executes them against the Blink renderer.
