#!/bin/bash
set -e

echo "Starting the installation process..."

# Unzip the deployment package
cd /opt/fastapi
if [ -f "deployment_package.zip" ]; then
    unzip deployment_package.zip
else
    echo "Deployment package not found!"
    exit 1
fi

# Install dependencies using pip
echo "Setting up virtual environment..."
source /opt/fastapi/venv/bin/activate
pip install -r requirements.txt

# Log successful installation
echo "Installation successful!" >> /var/log/fastapi/fastapi.log
