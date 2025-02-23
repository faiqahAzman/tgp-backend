#!/bin/bash
set -e

echo "Restoring .env file..."
if [ -f /tmp/.env_backup ]; then
    mv /tmp/.env_backup /opt/tgp-backend/.env
fi

echo "Setting correct ownership and permissions..."
chown -R ec2-user:ec2-user /opt/tgp-backend
chmod -R 755 /opt/tgp-backend

echo "Installing dependencies..."
pip install --upgrade pip
pip install --no-cache-dir -r /opt/tgp-backend/requirements.txt

echo "AfterInstall script completed."
