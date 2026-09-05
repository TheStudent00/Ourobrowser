#!/bin/bash
set -e

MOCK_FILE="v8_html_button_element.cc"
AST_OUT="mock_ur_ast.json"
CPP_OUT_DIR="python_bindings_output"

echo "=== 1. Running PseudoCoup Ingress (Mock) ==="
PYTHONPATH="$HOME/Programming/PseudoCoup" python3 -m pseudocoup.cli \
    --source "$MOCK_FILE" \
    --source-lang cpp \
    --ledger "../pc_ingress/pc_ledger_v8_sever.yaml" \
    --stage ingress-only \
    --out "$AST_OUT"

echo "=== 2. Running PseudoCoup Egress (Mock) ==="
mkdir -p "$CPP_OUT_DIR"
PYTHONPATH="$HOME/Programming/PseudoCoup" python3 -m pseudocoup.cli \
    --ast-input "$AST_OUT" \
    --target-lang cpp \
    --emitter-config "../pc_egress/py_emitter_config.yaml" \
    --outdir "$CPP_OUT_DIR"

echo "Mock Translation Complete! Check $CPP_OUT_DIR for PyDOM wrappers."
