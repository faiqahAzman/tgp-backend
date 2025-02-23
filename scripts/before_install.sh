#!/bin/bash
set -e

echo "Stopping FastAPI service..."
sudo systemctl stop tgp-backend || true  # Ignore errors if service is not running

echo "Preserving .env file..."
if [ -f /opt/tgp-backend/.env ]; then
    mv /opt/tgp-backend/.env /tmp/.env_backup
fi

echo "Removing old files..."
rm -rf /opt/tgp-backend/*

echo "BeforeInstall script completed."
