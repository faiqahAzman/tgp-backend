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

# Make all scripts executable
sudo chmod +x /opt/fastapi/scripts/*.sh

# Create FastAPI log directory
sudo mkdir -p /var/log/fastapi
sudo chown ec2-user:ec2-user /var/log/fastapi

# Create systemd service file
sudo tee /etc/systemd/system/fastapi.service << EOF
[Unit]
Description=FastAPI application
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/opt/fastapi
Environment="PATH=/opt/fastapi/venv/bin"
ExecStart=/opt/fastapi/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000 --workers 3
Restart=always

[Install]
WantedBy=multi-user.target
EOF

echo "FastAPI application installed and configured."
