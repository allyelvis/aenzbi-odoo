import unittest
import requests

class TestUserAcceptance(unittest.TestCase):
    BASE_URL = "http://localhost:5000"

    def test_product_flow(self):
        response = requests.post(f"{self.BASE_URL}/products", json={'name': 'Product1', 'price': 10})
        self.assertEqual(response.status_code, 201)
        product = response.json()
        self.assertEqual(product['name'], 'Product1')

        response = requests.get(f"{self.BASE_URL}/products")
        self.assertEqual(response.status_code, 200)
        products = response.json()
        self.assertGreater(len(products), 0)

    def test_invoice_flow(self):
        response = requests.post(f"{self.BASE_URL}/invoices", json={'invoice_number': 'INV1', 'amount': 100})
        self.assertEqual(response.status_code, 201)
        invoice = response.json()
        self.assertEqual(invoice['invoice_number'], 'INV1')

        response = requests.get(f"{self.BASE_URL}/invoices")
        self.assertEqual(response.status_code, 200)
        invoices = response.json()
        self.assertGreater(len(invoices), 0)

    def test_stock_movement_flow(self):
        response = requests.post(f"{self.BASE_URL}/stock_movements", json={'product_id': 1, 'quantity': 50})
        self.assertEqual(response.status_code, 201)
        stock_movement = response.json()
        self.assertEqual(stock_movement['product_id'], 1)

        response = requests.get(f"{self.BASE_URL}/stock_movements")
        self.assertEqual(response.status_code, 200)
        stock_movements = response.json()
        self.assertGreater(len(stock_movements), 0)

if __name__ == '__main__':
    unittest.main()
