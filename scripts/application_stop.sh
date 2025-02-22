#!/bin/bash
set -e

echo "Stopping FastAPI application..."
sudo systemctl stop fastapi
echo "FastAPI application stopped"
exit 0
