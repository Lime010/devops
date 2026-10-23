#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
source_dir=${1:-test}
[[ -d "$source_dir" ]] || { echo "source directory missing"; exit 1; }
mkdir -p backups
tar -czf "backups/$(date +%Y%m%d_%H%M%S)_$$.tar.gz" "$source_dir"
