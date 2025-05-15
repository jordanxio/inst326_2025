"""Main runner for the Inventory Management System.

Run this script from the command line to interact with the inventory system.
"""
#importing the core classes from your system
from inventory_system import Item, InventoryManager, SalesLogger, IOUtils


def main():
    #creating an instance of the classes of InventoryManager and SalesLogger
    inventory = InventoryManager()
    sales_logger = SalesLogger()

    #starting a loop that displays the main menu and processes user input
    while True:
        print("\n--- Inventory Management Menu ---")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. Search Items")
        print("5. View Inventory Summary")
        print("6. Log Sale")
        print("7. View Sales Report")
        print("8. Save Inventory")
        print("9. Load Inventory")
        print("10. Exit")

        #works with getting the user's menu choice
        choice = input("Enter choice (1-10): ")

         #adding a new item to the inventory
        if choice == '1':
            item_id = input("Item ID: ")
            name = input("Name: ")
            category = input("Category: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            discount = float(input("Discount (0-1): "))
            #then creating a new Item object and add it to the inventory
            item = Item(item_id, name, category, quantity, price, discount)
            inventory.add_item(item)
            print("Item added.")

        #removing an item by ID
        elif choice == '2':
            item_id = input("Enter Item ID to remove: ")
            inventory.remove_item(item_id)
            print("Item removed (if it existed).")

        #updating an item attributes (either price, quantity, or discount)
        elif choice == '3':
            item_id = input("Enter Item ID to update: ")
            attr = input("Attribute to update (price, quantity, discount): ")
            value = float(input("New value: "))
            inventory.update_item(item_id, attr, value)
            print("Item updated.")

        #search items by keywords (such as name or category)
        elif choice == '4':
            keyword = input("Enter keyword to search: ")
            results = inventory.search_items(keyword)
            for item in results:
                print(item.to_string())

        #displays inventory summary (total items, total value)
        elif choice == '5':
            summary = inventory.display_summary()
            print(f"Total Items: {summary['total_items']}")
            print(f"Total Inventory Value: ${summary['total_value']:.2f}")
            
         #logs a sale (updates inventory + logs transaction)
        elif choice == '6':
            item_id = input("Item ID: ")
            quantity_sold = int(input("Quantity Sold: "))
            #handles and checks if item exists in inventory
            if item_id in inventory.items:
                item = inventory.items[item_id]
                 #makes sures enough stock is available
                if item.quantity >= quantity_sold:
                    item.update_quantity(-quantity_sold)
                    sales_logger.log_sale(item_id, quantity_sold, item.get_total_price())
                    print("Sale logged.")
                else:
                    print("Not enough stock.")
            else:
                print("Item not found.")
        #views the sales report (total revenue and # of transactions)
        elif choice == '7':
            print(sales_logger.get_sales_report())

       #saves the inventory and sales to file 
        elif choice == '8':
            IOUtils.save_inventory("inventory.txt", inventory.items)
            IOUtils.save_sales("sales.txt", sales_logger.transactions)
            print("Inventory and sales saved to file.")
            
        #loads the inventory and sales from file
        elif choice == '9':
            inventory.items = IOUtils.load_inventory("inventory.txt")
            sales_logger.transactions = IOUtils.load_sales("sales.txt")
            print("Inventory and sales loaded from file.")

        #exits the loop
        elif choice == '10':
            print("Exiting...")
            break
        #handles input error,  invalid menu choices
        else:
            print("Invalid choice. Try again.")

#only run the program when the script is executed directly
if __name__ == "__main__":
    main()
