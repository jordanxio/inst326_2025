class Item:
    """Represents a single inventory item in the system.

    Attributes:
        item_id (str): A unique identifier for the item.
        name (str): The name of the item.
        category (str): The category the item belongs to.
        quantity (int): The number of units available in stock.
        price (float): The unit price of the item.
        discount (float): Discount rate applied to the item (between 0 and 1).
    """

    def __init__(self, item_id, name, category, quantity, price, discount = 0.0):
        """Initializes an Item object with the specified attributes.

        Args:
            item_id (str): Unique ID of the item.
            name (str): Name of the item.
            category (str): Category label.
            quantity (int): Quantity in stock.
            price (float): Price per unit.
            discount (float): Discount rate (0.0 to 1.0). Default is 0.
        """
      

    def update_price(self, new_price):
        """Updates the price of the item.

        Args:
            new_price (float): The new price to set. Must be non-negative.
        """
     

    def update_quantity(self, amount):
        """Updates the quantity of the item by the given amount.

        Args:
            amount (int): The amount to adjust the quantity by.
                Can be positive (restock) or negative (sale).

        Side effects:
            Modifies the value of quantity.
        """
       

    def apply_discount(self, discount_rate):
        """Applies a discount to the item.

        Args:
            discount_rate (float): A value between 0 and 1 representing the discount.

        Side effects:
            Modifies the value of discount.
        """
        

    def get_total_price(self):
        """Calculates the effective price after discount.

        Returns:
            float: The discounted price of the item.
        """
        

    def to_string(self):
        """Returns a string with a summary of the item's details.

        Returns:
            str: Summary string with ID, name, price, and other details.
        """
        
class InventoryManager:
    """Manages a collection of inventory items.

    Attributes:
        items (dict of str: Item): Maps item IDs to Item objects.
    """

    def __init__(self):
        """Initializes an empty inventory."""


    def add_item(self, item):
        """Adds a new item to the inventory.

        Args:
            item (Item): The item to add.

        Side effects:
            Modifies the items dictionary.
        """


    def remove_item(self, item_id):
        """Removes an item from the inventory by ID.

        Args:
            item_id (str): The ID of the item to remove.

        Side effects:
            Modifies the items dictionary.
        """
 

    def update_item(self, item_id, attribute, value):
        """Updates a specific attribute of an item.

        Args:
            item_id (str): ID of the item to update.
            attribute (str): Attribute to update ('price', 'quantity', or 'discount').
            value: New value to set.

        Side effects:
            Modifies the corresponding attribute of the Item.
        """
 

    def search_items(self, keyword):
        """Searches for items by keyword in their name or category.

        Args:
            keyword (str): Keyword to search for.

        Returns:
            list of Item: Matching items.
        """
    
    def display_summary(self):
        """Displays a summary of the inventory.

        Returns:
            dict: Summary including total number of items and total value.
        """
        
    def get_all_items(self):
        """Returns all items in the inventory.

        Returns:
            list of Item: All inventory items.
        """
class SalesLogger:
    """Logs and stores sales transactions.

    Attributes:
        transactions (list of dict): Each dictionary contains sale info such as
            item_id, quantity, total price, and timestamp.
    """

    def __init__(self):
        """Initializes an empty sales log."""
      

    def log_sale(self, item_id, quantity_sold, price_per_item):
        """Records a new sale.

        Args:
            item_id (str): ID of the sold item.
            quantity_sold (int): Number of units sold.
            price_per_item (float): Price per unit at time of sale.

        Side effects:
            Appends a transaction to the internal transaction log.
        """
     

    def get_sales_report(self):
        """Generates a summary report of total sales.

        Returns:
            str: Report showing number of transactions and total revenue.
        """
     

    def get_transactions(self):
        """Returns all recorded transactions.

        Returns:
            list of dict: Sales transactions.
        """
    
class IOUtils:
    """Handles reading and writing inventory and sales data to files."""

    def save_inventory(filename, items):
        """Saves inventory to a file.

        Args:
            filename (str): Path to the output file.
            items (dict of str: Item): Items to save.

        Side effects:
            Creates or overwrites a file.
        """
    
    def load_inventory(filename):
        """Loads inventory from a file.

        Args:
            filename (str): Path to the file containing inventory data.

        Returns:
            dict of str: Item: Reconstructed items from file.
        """


  
    def save_sales(filename, transactions):
        """Saves sales data to a file.

        Args:
            filename (str): Output file path.
            transactions (list of dict): Sales data to write.

        Side effects:
            Creates or overwrites a file.
        """
    

    def load_sales(filename):
        """Loads sales data from a file.

        Args:
            filename (str): File containing transaction data.

        Returns:
            list of dict: Parsed transaction records.
        """