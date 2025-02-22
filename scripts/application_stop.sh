#!/bin/bash
set -e

echo "Checking if FastAPI service exists..."
if systemctl list-unit-files | grep -q "fastapi.service"; then
    echo "Stopping FastAPI Application..."
    sudo systemctl stop fastapi.service || true
else
    echo "FastAPI service does not exist yet. Continuing..."
fi

# Backup logs if they exist
if [ -d "/var/log/fastapi" ]; then
    echo "Backing up logs..."
    sudo mkdir -p /opt/fastapi/logs_backup
    sudo cp /var/log/fastapi/* /opt/fastapi/logs_backup/ || true
fi