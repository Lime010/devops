#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
exec 9>/tmp/devops-midterm-reconcile.lock
flock -n 9 || exit 0
[[ -f .maintenance ]] && { echo "maintenance: skipped"; exit 0; }
running=$(docker compose ps --status running -q web | wc -l)
echo "$(date -Iseconds) running=$running desired=3"
if [[ "$running" -ne 3 ]]; then
  docker compose up -d --no-build --scale web=3 --wait --wait-timeout 90
fi
