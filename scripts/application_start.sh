#!/bin/bash
set -e

echo "Starting FastAPI application..."
cd /opt/fastapi
./start_server.sh

# Health check
for i in {1..30}; do
    if curl -s http://localhost:80/health; then
        echo "Application started successfully"
        exit 0
    fi
    echo "Waiting for application to start... ($i/30)"
    sleep 2
done

echo "Application failed to start within 60 seconds"
exit 1
