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
pip3 install gunicorn uvicorn

# Create a startup script
sudo tee /opt/fastapi/start_server.sh << EOF
#!/bin/bash
cd /opt/fastapi
source venv/bin/activate
exec gunicorn main:app \
    --workers 3 \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000 \
    --log-level info \
    --access-logfile /var/log/fastapi/access.log \
    --error-logfile /var/log/fastapi/error.log \
    --capture-output \
    --daemon
EOF

# Make the startup script executable
sudo chmod +x /opt/fastapi/start_server.sh