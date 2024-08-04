from flask import current_app as app, jsonify

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Aenzbi-Odoo!"})

@app.route('/about')
def about():
    return jsonify({"message": "This is the about page of Aenzbi-Odoo!"})
