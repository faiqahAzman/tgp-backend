#!/bin/bash
set -e

echo "Restarting FastAPI service..."

# Preserve existing .env file
if [ -f /opt/tgp-backend/.env ]; then
    echo ".env file exists, preserving it."
    mv /opt/tgp-backend/.env /tmp/.env_backup
fi

pip install --no-cache-dir -r /opt/tgp-backend/requirements.txt

# Ensure correct ownership
chown -R ec2-user:ec2-user /opt/tgp-backend
chmod -R 755 /opt/tgp-backend

# Restore .env file if it was moved
if [ -f /tmp/.env_backup ]; then
    mv /tmp/.env_backup /opt/tgp-backend/.env
    echo "Restored .env file."
fi

# Restart systemd service
sudo systemctl restart tgp-backend
echo "Service restarted successfully."
