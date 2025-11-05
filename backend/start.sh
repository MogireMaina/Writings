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

# Check for Firebase key
if [ ! -f "firebase-key.json" ]; then
    echo ""
    echo "⚠️  WARNING: firebase-key.json not found"
    echo "   Firebase features will be disabled"
    echo "   To enable Firebase:"
    echo "   1. Download service account key from Firebase Console"
    echo "   2. Save it as backend/firebase-key.json"
    echo ""
fi

# Start the server
echo "Starting backend server on port 44445..."
echo "=========================================="
python app.py
