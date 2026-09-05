#!/bin/bash
set -e

export PATH="$HOME/Programming/depot_tools:$PATH"
mkdir -p chromium_src
cd chromium_src

echo "Fetching chromium (no-history) to save space..."
fetch --no-history chromium

echo "Chromium fetch initiated/completed."
