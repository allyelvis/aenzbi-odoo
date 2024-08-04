#!/bin/bash

# Set up the environment
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "Environment setup completed."
