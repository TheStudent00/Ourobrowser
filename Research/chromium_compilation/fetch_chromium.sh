#!/bin/bash
set -e

export PATH="$HOME/Programming/depot_tools:$PATH"
mkdir -p ~/Programming/chromium_src
cd ~/Programming/chromium_src

echo "Fetching chromium (no-history) to save space..."
fetch --no-history chromium

echo "Chromium fetch initiated/completed."
