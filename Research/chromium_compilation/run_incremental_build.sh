#!/bin/bash
export PATH="$HOME/Programming/depot_tools:$PATH"
cd ~/Programming/chromium_src/src

echo "Running ninja... (Saving output to build_log.txt)"
ninja -C out/Default third_party/blink/renderer/bindings/core/v8 > build_log.txt 2>&1 || true

echo "Parsing errors..."
python3 ~/Programming/Ourobrowser/Research/chromium_compilation/ninja_error_parser.py build_log.txt
