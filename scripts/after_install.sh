#!/bin/bash
echo "Unzipping deployment package..."
cd /opt/fastapi
sudo rm -rf *  # Remove old files
sudo unzip /opt/fastapi/deployment_package.zip
sudo chown -R ec2-user:ec2-user /opt/fastapi