#!/usr/bin/env bash
set -euo pipefail

APP_URL="http://localhost:8000/admin/"  # Can change port

if [ "${1:-}" = "up" ]; then
    echo "Running containers..."
    docker compose up --build -d
    echo "Waiting for containers..."
    sleep 5
    until curl -s -f "$APP_URL" > /dev/null; do
        printf "."
        sleep 2
    done

    echo ""
    echo "Deploy completed. Application running on:"
    echo "  $APP_URL"
elif [ "${1:-}" = "down" ]; then
    echo "stopping containers..."
    docker compose down -v
else
 echo "Usage: $0 {up|down}"
 exit 1
fi