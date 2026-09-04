---
id: ourobrowser.root.research.pc_ingress
level: 2
status: draft
settled_by: Dee
supersedes: null
designation: pending
node:
    name: pc_ingress
    path: Planning/node_0_1_research/node_0_0_pc_ingress/CORE_0_0_pc_ingress.md
super_node:
    name: research
    path: ../CORE_0_1_research.md
sub_nodes: []
---

# CORE 0_0 — pc_ingress

## metadata

- **id:** ourobrowser.root.research.pc_ingress
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

**Goal:** Configure PseudoCoup (PC) to ingress the Chromium DOM-to-V8 bindings and WebIDL definitions.

**Details:**
- Target Chromium's `third_party/blink/renderer/bindings/` directory.
- This directory contains the WebIDL definitions and auto-generated C++ code that bridges Blink's internal DOM representation to V8 JavaScript objects.
- PC's `tree-sitter` parsers will map these bindings into the UR-AST. 
- The Ledger must be strictly configured to recognize the boundary: we are not translating the rendering engine itself (Blink), but rather the *interface* surface where Blink exposes objects to external scripts.
- We need to establish "stub points" where V8 specific types (`v8::Local`, `v8::Isolate`) are encountered, marking them as targets for replacement in the egress phase.
