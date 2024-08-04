import unittest
import json
from app import app

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_products(self):
        response = self.app.post('/products', data=json.dumps({'name': 'Product1', 'price': 10}), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Product1', response.data)

    def test_invoices(self):
        response = self.app.post('/invoices', data=json.dumps({'invoice_number': 'INV1', 'amount': 100}), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.app.get('/invoices')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'INV1', response.data)

    def test_stock_movements(self):
        response = self.app.post('/stock_movements', data=json.dumps({'product_id': 1, 'quantity': 50}), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.app.get('/stock_movements')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'product_id', response.data)

if __name__ == '__main__':
    unittest.main()
