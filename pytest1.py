import unittest

class TestItem(unittest.TestCase):
    def setUp(self):
        # hoodie 
        self.item = Item(item_id="1",name="Hoodie",category="Clothing",quantity=5,
                         price=75.00,discount=0.0)

    def test_update_price(self):
        # updates price 
        self.item.update_price(80.00)
        self.assertEqual(self.item.price, 80.00)

    def test_update_quantity(self):
        # remove 3 items 
        self.item.update_quantity(-3)
        self.assertEqual(self.item.quantity, 2)
        # add 10 items 
        self.item.update_quantity(10)
        self.assertEqual(self.item.quantity, 12)

    def test_apply_discount(self):
        # 15% discount
        self.item.apply_discount(0.15)
        self.assertEqual(self.item.discount, 0.15)
        self.assertEqual(self.item.price, 75.00)

    def test_get_total_price(self):
        self.item.quantity = 1
        # 15% discount
        self.item.apply_discount(0.15)
        # price of a hoodie after discount
        expected = 75.00 * 0.85
        self.assertEqual(self.item.get_total_price(), expected)


class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.manager = InventoryManager()
        self.hoodie = Item(item_id="1",name="Hoodie",category="Clothing",quantity=5,
                         price=75.00,discount=0.0)
        
    def test_add_item(self):
        # adds 1 hoodie into inventory
        self.manager.add_item(self.hoodie)
        self.assertIn("1", self.manager.items)

    def test_remove_item(self):
        self.manager.add_item(self.hoodie)
        # removes 1 hoodie from inventory
        self.manager.remove_item("1")
        self.assertNotIn("1", self.manager.items)

    def test_update_item(self): 
        self.manager.add_item(self.hoodie)
        # updates price of hoodie to 85
        self.manager.update_item("1", "price", 85)
        self.assertEqual(self.manager.items["1"].price, 85)
        
    
    def test_search_item(self):
        self.manager.add_item(self.hoodie)
        results = self.manager.search_items("Hoodie")
        self.assetEuqal(len(results), 1)
        self.assertEqual(results[0].item_id, "1")

        





