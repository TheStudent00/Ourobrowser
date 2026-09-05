#!/bin/bash
export PATH="/projects/depot_tools:$PATH"
cd /projects/chromium_src/src

echo "Running ninja... (Saving output to build_log.txt)"
ninja -C out/Default third_party/blink/renderer/core > build_log.txt 2>&1 || true

echo "Parsing errors..."
python3 /projects/Ourobrowser/Research/chromium_compilation/ninja_error_parser.py build_log.txt > ninja_errors.log
