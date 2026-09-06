---
id: ourobrowser.root.check
---

# CHECK — 0

Node `ourobrowser.root`. Status `draft`.

## check 1 — completeness

> a node being complete means its sub-nodes are complete. if a node is
> a leaf with no sub-nodes, it is complete.
>
> — Dee, 2026-07-31

    complete(node) = status is `settled` AND every sub-node complete

**Is this node settled?** **no** — `status: draft`.

**Sub-nodes:** tools, research, api, engine, bridge, test_page. Three of
the six carry no definition at all (`tools`, `api` are `*(pending)*`), so
the sub-tree cannot be complete either.

### verdict

**NOT COMPLETE** — status is not `settled`, and three sub-nodes are
undefined.

## check 2 — is every approach the project is pursuing named in the tree?

A node exists for the PyQt6 engine and for the Chromium swap. The
QuteBrowser fork has code on disk — `Research/Qutebrowser_Fork`, five
files changed or added — and **no node**. A reader of this tree cannot
find it.

**Answer: no.** Whether the fork becomes a node, and where it sits, is
Dee's to settle; PROTOCOL §2 reserves level-1 COREs to him.

## check 3 — does the tree conform?

    python3 ~/Programming/PlanPlan/framework/check_plans.py \
        ~/Programming/Ourobrowser/Planning

**Answer: yes**, as of 2026-09-06 — 0 errors. The one remaining warning,
`## sub_nodes` not being the first section, is carried by every
conforming tree in the estate (PseudoCoupHQ reports it on 131 COREs).
