# test_inventory_system.py

import unittest, os

class TestSalesLogger(unittest.TestCase):
    def setUp(self):
        mod = __import__('inventory_system')
        self.SalesLogger = mod.SalesLogger

    def test_log_and_get_transactions(self):
        logger = self.SalesLogger()
        # log one sale of 3 units
        logger.log_sale("I1", 3, 4.0)
        txns = logger.get_transactions()
        # exactly one transaction should be recorded
        self.assertEqual(len(txns), 1)

        txn = txns[0]
        # check that fields match what we logged
        self.assertEqual(txn["item_id"], "I1")
        self.assertEqual(txn["quantity_sold"], 3)
        self.assertEqual(txn["price_per_item"], 4.0)
        self.assertEqual(txn["total_price"], 12.0)
        # timestamp field must exist
        self.assertIn("timestamp", txn)

    def test_get_sales_report(self):
        logger = self.SalesLogger()
        # log two sales: 1×2 + 2×3 = $8 total
        logger.log_sale("A", 1, 2.0)
        logger.log_sale("B", 2, 3.0)
        report = logger.get_sales_report()
        # report must be a string mentioning 2 transactions and total $8.00
        self.assertIsInstance(report, str)
        self.assertIn("2", report)
        self.assertIn("8.00", report)


class TestIOUtils(unittest.TestCase):
    def setUp(self):
        mod = __import__('inventory_system')
        self.IOUtils = mod.IOUtils
        self.Item    = mod.Item
        self.inv_file   = "test_inv.json"
        self.sales_file = "test_sales.json"

    def tearDown(self):
        # remove any files we created
        for fn in (self.inv_file, self.sales_file):
            if os.path.exists(fn):
                os.remove(fn)

    def test_save_and_load_inventory(self):
        # make a one‐item inventory
        items = {
            "X": self.Item("X", "Name", "Cat", quantity=1, price=1.0)
        }
        # save to disk
        self.IOUtils.save_inventory(self.inv_file, items)
        self.assertTrue(os.path.exists(self.inv_file))

        # load back
        loaded = self.IOUtils.load_inventory(self.inv_file)
        # must have the same key and an Item object
        self.assertIn("X", loaded)
        self.assertEqual(loaded["X"].item_id, "X")
        self.assertEqual(loaded["X"].quantity, 1)

    def test_save_and_load_sales(self):
        # one transaction
        txns = [{
            "item_id": "X",
            "quantity_sold": 1,
            "price_per_item": 1.0,
            "total_price": 1.0,
            "timestamp": "2025-01-01T00:00:00"
        }]
        # save
        self.IOUtils.save_sales(self.sales_file, txns)
        self.assertTrue(os.path.exists(self.sales_file))

        # load
        loaded = self.IOUtils.load_sales(self.sales_file)
        # loaded data must exactly match what we saved
        self.assertEqual(loaded, txns)


if __name__ == "__main__":
    unittest.main()
