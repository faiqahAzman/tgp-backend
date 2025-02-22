#!/bin/bash
set -e

echo "Preparing for FastAPI installation..."

# Install Python and development tools if not present
sudo dnf update -y
sudo dnf install -y python3 python3-pip python3-devel gcc

# Create necessary directories
sudo mkdir -p /opt/fastapi
sudo mkdir -p /var/log/fastapi

# Create log files if they don't exist
sudo touch /var/log/fastapi/fastapi.log
sudo touch /var/log/fastapi/fastapi.error.log

# Set proper permissions
sudo chown -R ec2-user:ec2-user /var/log/fastapi
sudo chown -R ec2-user:ec2-user /opt/fastapi

# Setup Python virtual environment
cd /opt/fastapi
python3 -m venv venv