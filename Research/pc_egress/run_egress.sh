#!/bin/bash
set -e

INPUT_AST="../pc_ingress/ur_ast_chromium_bindings.json"
EMITTER_CONFIG="py_emitter_config.yaml"
OUTPUT_DIR="../../../third_party/blink/renderer/bindings/core/python/"

echo "Starting PseudoCoup Egress Phase..."
echo "AST Input: $INPUT_AST"

python3 -m pseudocoup.cli \
    --ast-input "$INPUT_AST" \
    --target-lang cpp \
    --emitter-config "$EMITTER_CONFIG" \
    --outdir "$OUTPUT_DIR"

echo "Egress complete. PyDOM bindings generated in $OUTPUT_DIR."
