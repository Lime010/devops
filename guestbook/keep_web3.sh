#!/usr/bin/env bash
set -uo pipefail
cd "$(dirname "$0")" || exit 1
INTERVAL=${INTERVAL:-5}
[[ "$INTERVAL" =~ ^[1-9][0-9]*$ ]] || { echo "INTERVAL must be positive integer"; exit 1; }
trap 'echo "watcher stopped"; exit 0' INT TERM
while true; do
  if ! ./reconcile.sh; then
    echo "$(date -Iseconds) reconcile failed; retry next interval" >&2
  fi
  sleep "$INTERVAL" & wait $! || true
done
