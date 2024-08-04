from flask import Blueprint, request, jsonify

api = Blueprint('api', __name__)

products = []
invoices = []
stock_movements = []

@api.route('/products', methods=['GET', 'POST'])
def products_route():
    if request.method == 'POST':
        product = request.json
        products.append(product)
        return jsonify(product), 201
    return jsonify(products), 200

@api.route('/invoices', methods=['GET', 'POST'])
def invoices_route():
    if request.method == 'POST':
        invoice = request.json
        invoices.append(invoice)
        return jsonify(invoice), 201
    return jsonify(invoices), 200

@api.route('/stock_movements', methods=['GET', 'POST'])
def stock_movements_route():
    if request.method == 'POST':
        stock_movement = request.json
        stock_movements.append(stock_movement)
        return jsonify(stock_movement), 201
    return jsonify(stock_movements), 200
