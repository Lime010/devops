#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
command -v python3 >/dev/null || { echo "python3 required"; exit 1; }
curl -fsS http://127.0.0.1:11434/api/tags >/dev/null
exec python3 chat.py
