from flask import Flask, request, render_template, redirect, url_for, flash
import subprocess
import os
import aenzbi_odoo  # Importing the aenzbi-odoo package

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change this to a random key for production

# Odoo connection details
ODOO_URL = 'http://localhost:8069'
ODOO_DB = 'your_db'
ODOO_USER = 'admin'
ODOO_PASSWORD = 'admin'

# Initialize Odoo client
odoo_client = aenzbi_odoo.Client(ODOO_URL, ODOO_DB, ODOO_USER, ODOO_PASSWORD)

# Route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission
@app.route('/create_user', methods=['POST'])
def create_user():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        flash('Username and password are required!')
        return redirect(url_for('index'))

    # Use aenzbi-odoo to create a user in Odoo
    try:
        user_id = odoo_client.create_user(username, password)
        flash(f'User {username} created successfully in Odoo with ID {user_id}!')
    except Exception as e:
        flash(f'Error creating user: {e}')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
