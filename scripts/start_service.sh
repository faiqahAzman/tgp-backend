#!/bin/bash
set -e

echo "Starting FastAPI service..."
sudo systemctl restart tgp-backend

echo "Deployment complete!"
