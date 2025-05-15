
"""
inventory_system.py

Authors: Jordan Xiong, Fechi Iwudyke, Nhandi Nyawela, Jonathan Bui
Professor: Gaberiel Cruz
Class: INST326 (Section 0401)
Due Date: 05_16_2025

Challenges Encountered: Had a hard time trying to work with OOP in a real world application for data handling.
This code had basically no rubric or limitations so it made it hard to pin point what we wanted, what to do, how to it, etc.
Two different type of file handling with Sales Logger and Inventory management. That being said, those two were the hardest
classes to work with. With the help of knowing Unity//C# in earlier courses, the main.py was easier to work around
such as calling functions and working with handling. 

"""
#importing the datetime module to record sale timestamps later (this is the only thing we are importing)
from datetime import datetime

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
        self.item_id = item_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

        #value from 0 to 1 (so for example, 0.20 means 20% off)
        self.discount = discount

    def update_price(self, new_price):
        """Updates the price of the item.

        Args:
            new_price (float): The new price to set. Must be non-negative.
        """
        if new_price >= 0:
            #sets the new price
            self.price = new_price 
        #if the new price is negative, we don't change anything

    def update_quantity(self, amount):
        """Updates the quantity of the item by the given amount.

        Args:
            amount (int): The amount to adjust the quantity by.
                Can be positive (restock) or negative (sale).

        Side effects:
            Modifies the value of quantity.
        """
        new_quantity = self.quantity + amount
        if new_quantity >= 0:
            #update and replace
            self.quantity = new_quantity

    def apply_discount(self, discount_rate):
        """Applies a discount to the item.

        Args:
            discount_rate (float): A value between 0 and 1 representing the discount.

        Side effects:
            Modifies the value of discount.
        """
        if 0 <= discount_rate <= 1:
            #update and replace
            self.discount = discount_rate

    def get_total_price(self):
        """Calculates the effective price after discount.

        Returns:
            float: The discounted price of the item.
        """
        return self.price * (1 - self.discount)

    #similar to a repo, but bc im familiar with java we will just use something like a ToString
    def to_string(self):
        """Returns a string with a summary of the item's details.

        Returns:
            str: Summary string with ID, name, price, and other details.
        """
        return (f"ID: {self.item_id}, Name: {self.name}, Category: {self.category}, "
                f"Quantity: {self.quantity}, Price: ${self.price:.2f}, "
                f"Discount: {self.discount * 100:.0f}%, Total Price: ${self.get_total_price():.2f}")
        
class InventoryManager:
    """Manages a collection of inventory items.

    Attributes:
        items (dict of str: Item): Maps item IDs to Item objects.
    """

    def __init__(self):
        """Initializes an empty inventory.
         Args:
            self (object): The item object being initialize.
        """
        #empty
        self.items = {}

    def add_item(self, item):
        """Adds a new item to the inventory.
        
        Args:
            item (Item): The item to add.

        Side effects:
            Modifies the items dictionary.
        """
        #checks if the item ID is not already in the inventory
        if item.item_id not in self.items:
            #add to dict
            self.items[item.item_id] = item

    def remove_item(self, item_id):
        """Removes an item from the inventory by ID.

        Args:
            item_id (str): The ID of the item to remove.

        Side effects:
            Modifies the items dictionary.
        """
        if item_id in self.items:
            del self.items[item_id]


    def update_item(self, item_id, attribute, value):
        """Updates a specific attribute of an item.

        Args:
            item_id (str): ID of the item to update.
            attribute (str): Attribute to update ('price', 'quantity', or 'discount').
            value: New value to set.

        Side effects:
            Modifies the corresponding attribute of the Item.
        """
        #checks that the item exists in the inventory
        if item_id in self.items:
            item = self.items[item_id]
            #uses the appropriate method based on attribute name
            if attribute == 'price':
                item.update_price(value)
            elif attribute == 'quantity':
                item.update_quantity(value)
            elif attribute == 'discount':
                item.apply_discount(value)

    def search_items(self, keyword):
        """Searches for items by keyword in their name or category.

        Args:
            keyword (str): Keyword to search for.

        Returns:
            list of Item: Matching items.
        """
        result = []
        #loops through all items in the inventory
        for item in self.items.values():
             #checks if keyword is in the name or category (case-insensitive)
            if keyword.lower() in item.name.lower() or keyword.lower() in item.category.lower():
                result.append(item)
        #adds the item to the result list
        return result
    
    def display_summary(self):
        """Displays a summary of the inventory.

        Returns:
            dict: Summary including total number of items and total value.
        """
        total_items = len(self.items)
        total_value = sum(item.get_total_price() * item.quantity for item in self.items.values())
        #total value = discounted price × quantity
        return {
            'total_items': total_items,
            'total_value': total_value
        }
    def get_all_items(self):
        """Returns all items in the inventory.

        Returns:
            list of Item: All inventory items.
        """
        #converts dictionary values to a list
        return list(self.items.values())
    
class SalesLogger:
    """Logs and stores sales transactions.

    Attributes:
        transactions (list of dict): Each dictionary contains sale info such as
            item_id, quantity, total price, and timestamp.
    """

    def __init__(self):
        """Initializes an empty sales log."""
        self.transactions = []
    

    def log_sale(self, item_id, quantity_sold, price_per_item):
        """Records a new sale.

        Args:
            item_id (str): ID of the sold item.
            quantity_sold (int): Number of units sold.
            price_per_item (float): Price per unit at time of sale.

        Side effects:
            Appends a transaction to the internal transaction log.
        """
        transaction = {
            'item_id': item_id,
            'quantity_sold': quantity_sold,
            'price_per_item': price_per_item,
            'total_price': quantity_sold * price_per_item,
            #current date and time in standard format
            'timestamp': datetime.now().isoformat()
        }
        self.transactions.append(transaction)
     

    def get_sales_report(self):
        """Generates a summary report of total sales.

        Returns:
            str: Report showing number of transactions and total revenue.
        """
        #calc total revenue by adding up all the 'total_price' values
        total_revenue = sum(t['total_price'] for t in self.transactions)
        return f"Total transactions: {len(self.transactions)}, Total revenue: ${total_revenue:.2f}"
     

    def get_transactions(self):
        """Returns all recorded transactions.

        Returns:
            list of dict: Sales transactions.
        """
        
        return self.transactions
    
class IOUtils:
    """Handles reading and writing inventory and sales data to files.
    
    What is a @staticmethod:
    Static methods in Python are methods that belong to a class rather than an instance of the class.
    They are defined using the @staticmethod decorator and do not require an instance of the class to be called.
    Static methods do not have access to the instance (self) or class (cls) variables and are used when some functionality
    is related to the class but does not need to access or modify the class or instance state.
    """

    @staticmethod
    def save_inventory(filename, items):
        """Saves inventory to a file.

        Args:
            filename (str): Path to the output file.
            items (dict of str: Item): Items to save.

        Side effects:
            Creates or overwrites a file.
        """
        # Open the file in write mode ('w') which erases existing content
        with open(filename, 'w') as file:
            #goes through each item in the inventory
            for item in items.values():
                #format the item data into one line of comma-separated values
                line = f"{item.item_id},{item.name},{item.category},{item.quantity},{item.price},{item.discount}\n"
                #writes the line to the file
                file.write(line)
    
    @staticmethod
    def load_inventory(filename):
        """Loads inventory from a file.

        Args:
            filename (str): Path to the file containing inventory data.

        Returns:
            dict of str: Item: Reconstructed items from file.
        """
        #creates an empty dictionary to hold the items we load
        items = {}
        
        #opening the file in read mode ('r')
        with open(filename, 'r') as file:
            for line in file:
                
                #removing any whitespace at the end of the line and split by commas
                parts = line.strip().split(',')
                if len(parts) == 6:
                    #assign each part to a variable
                    item_id, name, category, quantity, price, discount = parts

                    #create a new Item using the loaded data
                    items[item_id] = Item(
                        item_id=item_id,
                        name=name,
                        category=category,
                        #convert datatype
                        quantity=int(quantity),
                        price=float(price),
                        discount=float(discount)
                    )
        return items

    @staticmethod
    def save_sales(filename, transactions):
        """Saves sales data to a file.

        Args:
            filename (str): Output file path.
            transactions (list of dict): Sales data to write.

        Side effects:
            Creates or overwrites a file.
        """
        #opens the file for writing
        with open(filename, 'w') as file:
            for transaction in transactions:
                 #converts the transaction dict to a CSV line
                line = f"{transaction['item_id']},{transaction['quantity_sold']},{transaction['total_price']},{transaction['timestamp']}\n"
                file.write(line)
    
    @staticmethod
    def load_sales(filename):
        """Loads sales data from a file.

        Args:
            filename (str): File containing transaction data.

        Returns:
            list of dict: Parsed transaction records.
        """
        transactions = []
        #opens the file in read mode
        with open(filename, 'r') as file:
            for line in file:
                #split each line into fields
                item_id, quantity_sold, total_price, timestamp = line.strip().split(',')
                
                #creats a dictionary from the data and append it to the list
                transactions.append({
                    'item_id': item_id,
                    'quantity_sold': int(quantity_sold),
                    'total_price': float(total_price),
                    'timestamp': timestamp
                })
        return transactions
