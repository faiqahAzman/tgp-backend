echo "Installing FastAPI application..."
cd /opt/fastapi

# Ensure virtual environment exists.  Create if it doesn't.
if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv venv
fi

# Set permissions - IMPORTANT FOR SECURITY
sudo chown -R ec2-user:ec2-user /opt/fastapi  #Ensure the current user has the right privileges

# Activate virtual environment and install dependencies
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
pip3 install gunicorn uvicorn

# Create FastAPI log directory
sudo mkdir -p /var/log/fastapi
sudo chown ec2-user:ec2-user /var/log/fastapi

# Create a startup script
sudo tee /opt/fastapi/start_server.sh << 'EOF'
#!/bin/bash
source venv/bin/activate
exec gunicorn main:app \
    --workers 3 \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000 \
    --log-level info \
    --access-logfile /var/log/fastapi/access.log \
    --error-logfile /var/log/fastapi/error.log
EOF

# Make the startup script executable
sudo chmod +x /opt/fastapi/start_server.sh
sudo chown ec2-user:ec2-user /opt/fastapi/start_server.sh

echo "FastAPI application installed and configured."
