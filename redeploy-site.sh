#!/bin/bash

echo "Moving into project directory..."
cd ~/pe-portfolio-site

echo "Pulling latest code from GitHub..."
git fetch origin
git reset --hard origin/main

echo "Activating virtual environment..."
source python3-virtualenv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Update service"
systemctl daemon-reload
systemctl restart myportfolio

echo "Redeploy complete."