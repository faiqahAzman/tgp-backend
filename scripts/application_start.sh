#!/bin/bash
set -e

echo "Starting FastAPI application..."
cd /opt/fastapi
source venv/bin/activate

# Log startup
echo "$(date): Starting FastAPI application" >> /var/log/fastapi/startup.log

# Run uvicorn directly
exec uvicorn main:app \
    --host 0.0.0.0 \
    --workers 3 \
    --log-level info \
    --access-log
