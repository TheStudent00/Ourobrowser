#!/bin/bash
export PATH="/projects/depot_tools:$PATH"
cd /projects/chromium_src/src

MAX_ITERATIONS=5
for ((i=1; i<=MAX_ITERATIONS; i++)); do
    echo "--- TRICKLE ITERATION $i ---"
    
    echo "Running ninja... (Saving output to build_log.txt)"
    ninja -C out/Default third_party/blink/renderer/core > build_log.txt 2>&1
    if [ $? -eq 0 ]; then
        echo "Build succeeded! Trickle complete."
        exit 0
    fi
    
    echo "Parsing errors..."
    python3 /projects/Ourobrowser/Research/chromium_compilation/ninja_error_parser.py build_log.txt > ninja_errors.log
    
    # Check if there are failed files
    if ! grep -q "^../../third_party" ninja_errors.log; then
        echo "No transpilable failed files found. Stopping trickle."
        exit 1
    fi
    
    echo "Transpiling failed files..."
    python3 /projects/Ourobrowser/Research/chromium_compilation/transpiler_loop.py
    
    echo "Iteration $i complete. Looping..."
done

echo "Trickle paused after $MAX_ITERATIONS iterations."
