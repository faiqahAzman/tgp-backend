#!/bin/bash
set -e

echo "Installing FastAPI application..."
cd /opt/fastapi

# Clean and unzip new deployment
sudo rm -rf *  # Remove old files
sudo unzip deployment_package.zip

# Set permissions
sudo chown -R ec2-user:ec2-user /opt/fastapi

# Activate virtual environment and install dependencies
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt

# Create systemd service file
sudo tee /etc/systemd/system/fastapi.service << EOF
[Unit]
Description=FastAPI application
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/opt/fastapi
Environment="PATH=/opt/fastapi/venv/bin"
ExecStart=/opt/fastapi/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always
StandardOutput=append:/var/log/fastapi/fastapi.log
StandardError=append:/var/log/fastapi/fastapi.error.log

[Install]
WantedBy=multi-user.target
EOF

# Reload systemd and enable service
sudo systemctl daemon-reload
sudo systemctl enable fastapi.service