#!/bin/bash

# Navigate to the project directory
cd flask_user_management

# Set up the environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Instructions
echo "Setup complete. To run the application, use 'python app.py'."
