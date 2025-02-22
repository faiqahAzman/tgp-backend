#!/bin/bash
set -e

echo "Checking for existing FastAPI process..."
if pgrep -f "gunicorn main:app"; then
    echo "Stopping existing FastAPI process..."
    sudo pkill -f "gunicorn main:app" || true
fi

# Backup logs if they exist
if [ -d "/var/log/fastapi" ]; then
    echo "Backing up logs..."
    sudo mkdir -p /opt/fastapi/logs_backup
    sudo cp /var/log/fastapi/* /opt/fastapi/logs_backup/ || true
fi