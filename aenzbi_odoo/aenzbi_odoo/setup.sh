#!/bin/bash

# Set up the environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Instructions
echo "Setup complete. To run the application, use 'python app.py'."
echo "To run tests, use 'python -m unittest discover -s tests/unit', 'python -m unittest discover -s tests/integration', and 'python -m unittest discover -s tests/uat'."
