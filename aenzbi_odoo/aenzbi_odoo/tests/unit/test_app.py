import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_products(self):
        response = self.app.post('/products', json={'name': 'Product1', 'price': 10})
        self.assertEqual(response.status_code, 201)

        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Product1', response.data)

    def test_invoices(self):
        response = self.app.post('/invoices', json={'invoice_number': 'INV1', 'amount': 100})
        self.assertEqual(response.status_code, 201)

        response = self.app.get('/invoices')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'INV1', response.data)

    def test_stock_movements(self):
        response = self.app.post('/stock_movements', json={'product_id': 1, 'quantity': 50})
        self.assertEqual(response.status_code, 201)

        response = self.app.get('/stock_movements')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'product_id', response.data)

if __name__ == '__main__':
    unittest.main()
