#!/bin/bash

echo "📦 [1/5] Updating system packages..."
sudo apt update && sudo apt upgrade -y

echo "🐍 [2/5] Installing Python3 and pip..."
sudo apt install python3 python3-pip -y

echo "🔧 [3/5] Installing Git..."
sudo apt install git -y

echo "📁 [4/5] Creating and activating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "📦 [5/5] Installing Python packages from requirements.txt..."
pip install -r requirements.txt

echo "✅ Setup complete. Virtual environment activated."

