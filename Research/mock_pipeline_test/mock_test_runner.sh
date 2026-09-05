#!/bin/bash
set -e

MOCK_FILE="v8_html_button_element.cc"

PC_V3_DIR="$HOME/Programming/Ourobrowser/Tools/PCv3.1"

echo "=== Running PseudoCoup V3 (Mock) ==="
PYTHONPATH="$PC_V3_DIR" python3 -m pseudocoup.cli \
    --source "$MOCK_FILE" \
    --source-lang cpp \
    --target-lang cpp

echo "Mock Translation Complete!"
