#!/bin/bash

echo "=========================================="
echo "AI Fine-tuning Data Prep - Backend Startup"
echo "=========================================="

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate venv
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -q -r requirements.txt

# Start the server
echo "Starting backend server on port 44445..."
echo "=========================================="
python app.py
