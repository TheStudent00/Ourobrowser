---
id: ourobrowser.root.research.pc_tools.check
---

# CHECK — 0_1_3_pc_tools

Node `ourobrowser.root.research.pc_tools`. Status `settled`.

## check 1 — completeness

    complete(node) = status is `settled` AND every sub-node complete

**Is this node settled?** **yes** — `status: settled`

**Sub-nodes:** *none — this is a leaf.*

### verdict

**COMPLETE** — a settled leaf.

## check 2 — does a C++ source survive a round trip?

A file read by the C++ ingress and written straight back out by the C++
emitter must differ only where a mapping was asked for. Measured
2026-09-06 over the seven Chromium headers the trickle loop had already
rewritten: each one comes back with 4 or 5 lines differing out of 44 to
414, and none loses a class body. Before the same day's work, six of the
seven came back as 6 lines total.

Evidence: `DevComms/log_002_transpiler_keeps_the_source.md` §2.
