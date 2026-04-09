#!/usr/bin/env bash
set -e

# Install gh CLI if missing
if ! command -v gh &>/dev/null; then
    echo "[startup] Installing gh CLI..."
    (type -p wget >/dev/null || (sudo apt-get update && sudo apt-get install wget -y)) \
        && sudo mkdir -p -m 755 /etc/apt/keyrings \
        && out=$(mktemp) && wget -nv -O"$out" https://cli.github.com/packages/githubcli-archive-keyring.gpg \
        && cat "$out" | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
        && sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
        && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
        && sudo apt-get update && sudo apt-get install gh -y
fi

# Install Python dependencies if missing
pip3 install --quiet fal-client 2>/dev/null || true

# Check FAL_KEY
if [ -z "$FAL_KEY" ]; then
    echo ""
    echo "WARNING: FAL_KEY environment variable is not set."
    echo "Image generation (generate-image.py) will not work without it."
    echo "Set it before running: export FAL_KEY=your-key-here"
    echo ""
fi
