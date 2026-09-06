#!/bin/bash
# Run every mock binding in this folder through PCv3.1 (C++ -> C++) with the
# SAME type and function mapping tables the trickle loop uses, so what this
# folder shows is what the loop would do to a real Blink file.
#
#   bash ~/Programming/Ourobrowser/Research/mock_pipeline_test/mock_test_runner.sh
#
# Each <name>.cc produces <name>.cpp beside it and <name>.ledger.json (the
# mapping tables, plus every written type PCv3.1 registered while reading).
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
OURO="$(cd "$HERE/../.." && pwd)"
PC_V3_DIR="$OURO/Tools/PCv3.1"
LOOP="$OURO/Research/chromium_compilation"

cd "$HERE"
for src in *.cc; do
    name="${src%.cc}"
    PYTHONPATH="$LOOP" python3 -c "import transpiler_loop as t; t.write_ledger('$name.ledger.json')"
    echo "=== $src ==="
    PYTHONPATH="$PC_V3_DIR" python3 -m pseudocoup.cli \
        --source "$src" --source-lang cpp --target-lang cpp
    cat "$name.cpp"
    echo
done
echo "Mock translation complete."
