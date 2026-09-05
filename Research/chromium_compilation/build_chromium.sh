#!/bin/bash
set -e

CHROMIUM_DIR="../../../"
cd "$CHROMIUM_DIR"

echo "Applying GN Patch..."
patch -p0 < Research/chromium_compilation/build_v8_to_python.patch

echo "Configuring GN arguments (use_v8=false)..."
gn gen out/Ourobrowser --args="use_v8=false enable_nacl=false is_component_build=true"

echo "Compiling Chromium..."
autoninja -C out/Ourobrowser chrome

echo "Compilation complete."
