#!/bin/bash
set -e

echo "Starting FastAPI application..."

# Reload systemd and start service
sudo systemctl daemon-reload
sudo systemctl start fastapi
sudo systemctl enable fastapi

echo "FastAPI application started"
exit 0
