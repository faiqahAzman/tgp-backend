#!/bin/bash
set -e

echo "Stopping FastAPI application..."

# Find and kill any running uvicorn processes
pkill -f "uvicorn main:app" || true

echo "FastAPI application stopped"
