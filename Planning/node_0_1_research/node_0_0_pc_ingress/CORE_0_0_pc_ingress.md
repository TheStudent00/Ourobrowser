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

## super_node
- [research](../CORE_0_1_research.md)

## definition
Configure PseudoCoup (PC) to ingress the Chromium DOM-to-V8 bindings. We target `third_party/blink/renderer/bindings/` to map the C++ glue code into PC's UR-AST, explicitly severing all deep dependencies on the V8 JavaScript engine.

## design

**1. Ledger Configuration (`pc_ledger_v8_sever.yaml`)**
We must define a strict PC Ledger file to guide the `tree-sitter` parser. It will map structural interfaces but classify all V8-specific engine types as abstract "Dead Ends".
```yaml
ingress:
  source_lang: cpp
  target_dirs:
    - "third_party/blink/renderer/bindings/core/v8/"
  dead_ends:
    - "v8::Isolate"
    - "v8::Local"
    - "v8::HandleScope"
    - "v8::Context"
    - "v8::FunctionCallbackInfo"
```

**2. The Ingress Runner (`run_ingress.sh`)**
A deterministic script to execute the PC pipeline and output the UR-AST.
```bash
python3 -m pseudocoup.cli \
    --source third_party/blink/renderer/bindings/core/v8/ \
    --source-lang cpp \
    --ledger pc_ledger_v8_sever.yaml \
    --stage ingress-only \
    --out ur_ast_chromium_bindings.json
```

## settled rules
- **Strict Boundary Enforcement:** PC must explicitly fail if it attempts to resolve a C++ `#include <v8.h>` that is not covered by the `dead_ends` ledger config. We do not want to accidentally map the internal V8 compiler into our UR-AST.
- **Target Restriction:** We are strictly ingesting the `bindings/core/v8` directory. We are *not* ingesting the core Blink DOM logic (`third_party/blink/renderer/core/`), as the underlying DOM rendering math remains perfectly functional without modification.
