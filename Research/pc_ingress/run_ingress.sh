#!/bin/bash
set -e

# PC Ingress Runner Script
# Maps Chromium's V8 Bindings to a UR-AST, explicitly severing V8 engine dependencies.

CHROMIUM_SRC_DIR=${1:-"../../../third_party/blink/renderer/bindings/core/v8/"}
LEDGER_FILE="pc_ledger_v8_sever.yaml"
OUTPUT_FILE="ur_ast_chromium_bindings.json"

echo "Starting PseudoCoup Ingress Phase..."
echo "Target: $CHROMIUM_SRC_DIR"
echo "Ledger: $LEDGER_FILE"

python3 -m pseudocoup.cli \
    --source "$CHROMIUM_SRC_DIR" \
    --source-lang cpp \
    --ledger "$LEDGER_FILE" \
    --stage ingress-only \
    --out "$OUTPUT_FILE"

echo "Ingress complete. UR-AST saved to $OUTPUT_FILE."
