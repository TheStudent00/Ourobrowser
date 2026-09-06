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
sub_nodes:
    - name: gn_patch
      path: node_0_0_gn_patch/CORE_0_0_gn_patch.md
    - name: build_runner
      path: node_0_1_build_runner/CORE_0_1_build_runner.md
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

Modify the Chromium build system (GN/Ninja) to exclude V8 compilation, link the embedded CPython library, and compile our newly emitted `PyDOM` C++ bindings into the Blink renderer.

## design

**1. GN Build Patch (`build_v8_to_python.patch`)**
A patch file applied to Chromium's GN configuration to alter the dependency graph.
- Modify `third_party/blink/renderer/bindings/BUILD.gn`: Remove `//v8` from `deps`.
- Add a new custom target `//build/config/python:embed` which dynamically links `libpython3.so` (or statically compiles Python if cross-platform distribution is required).
- Instruct GN to glob `third_party/blink/renderer/bindings/core/python/*.cc` instead of `core/v8/*.cc`.

**2. Compilation Runner (`build_chromium.sh`)**
```bash
# Generate Ninja files with V8 explicitly disabled in args.gn
gn gen out/Ourobrowser --args="use_v8=false enable_nacl=false is_component_build=true"

# Compile the full browser frontend
autoninja -C out/Ourobrowser chrome
```

## settled rules
- **Zero V8 Footprint:** The final compiled binary (`chrome` or `ourobrowser`) must not link against `v8.dll` or `libv8.so`. If V8 symbols are required for linkage, the build is considered poisoned and must fail.
- **Dynamic Python Linking:** For prototyping, we will dynamically link the system's `libpython3`. Static compilation will be deferred to a later deployment node.
