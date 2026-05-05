import unittest
import os
import json
from order_system import OrderSystem

class TestOrderSystem(unittest.TestCase):
    def setUp(self):
        self.test_db = "test_orders.json"
        # Monkey patch the DB_FILE for testing
        OrderSystem.DB_FILE = self.test_db
        self.system = OrderSystem()

    def tearDown(self):
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_add_order(self):
        items = {"papitas": 2, "helados": 1}
        success = self.system.add_order("101", "Test Client", items)
        self.assertTrue(success)
        self.assertIn("101", self.system.orders)
        self.assertEqual(self.system.orders["101"]["total"], 3500*2 + 1500*1)

    def test_duplicate_order(self):
        self.system.add_order("102", "Client A", {"agua": 1})
        success = self.system.add_order("102", "Client B", {"agua": 1})
        self.assertFalse(success)

    def test_cancel_order(self):
        self.system.add_order("103", "Client C", {"empanadas": 1})
        self.system.cancel_order("103")
        self.assertEqual(self.system.orders["103"]["estado"], "cancelado")

if __name__ == "__main__":
    unittest.main()
