#!/bin/bash
set -e

SERVICE_NAME="tgp-backend"

echo "Waiting 10 seconds for the service to stabilize..."
sleep 10

SYSTEMD_STATUS=$(systemctl is-active $SERVICE_NAME)

if [ "$SYSTEMD_STATUS" == "active" ]; then
    echo "✅ Service '$SERVICE_NAME' is running successfully."
    exit 0
else
    echo "❌ Service '$SERVICE_NAME' is NOT running. Check logs using:"
    echo "   sudo journalctl -u $SERVICE_NAME --no-pager -n 50"
    exit 1
fi
