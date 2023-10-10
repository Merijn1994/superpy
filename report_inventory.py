import csv
import os
from rich.console import Console
from rich.table import Table
from datetime import datetime

# Define file paths for the bought and sold item data
BOUGHT_FILE_PATH = os.path.join(os.getcwd(), 'data', 'bought.csv')
SOLD_FILE_PATH = os.path.join(os.getcwd(), 'data', 'sold.csv')

# Function to retrieve and process inventory data from CSV files
def get_inventory(date=None):
    # Create an empty dictionary to store bought items
    bought_items = {}
    
    # Open and read the 'bought.csv' file
    with open(BOUGHT_FILE_PATH, mode='r') as file:
        reader = csv.DictReader(file)
        
        # Iterate through rows in the CSV
        for row in reader:
            # Create a unique key for each bought item
            key = (row['product_name'].lower(), float(row['buy_price']), row['expiration_date'])
            
            # Check if the item already exists in the dictionary, if not, initialize it
            if key not in bought_items:
                bought_items[key] = {
                    'bought_ids': set(),
                    'product_name': row['product_name'].lower(),
                    'buy_price': float(row['buy_price']),
                    'expiration_date': row['expiration_date'],
                    'quantity': 0,
                }
            
            # Update the quantity and add the bought ID to the set
            bought_items[key]['quantity'] += 1
            bought_items[key]['bought_ids'].add(row['id'])

    # Open and read the 'sold.csv' file
    with open(SOLD_FILE_PATH, mode='r') as file:
        reader = csv.DictReader(file)
        
        # Iterate through rows in the CSV
        for row in reader:
            bought_id = row['bought_id']
            
            # Update the quantity of sold items in the bought_items dictionary
            for item in bought_items.values():
                if bought_id in item['bought_ids']:
                    item['quantity'] -= 1

    # Create a list to store the final inventory
    inventory = []
    
    # Filter items with a positive quantity (items still in stock on the specified date)
    for item in bought_items.values():
        if date is None or datetime.strptime(item['expiration_date'], '%Y-%m-%d').date() >= date:
            if item['quantity'] > 0:
                inventory.append(item)
    
    return inventory

# Function to print the inventory using a rich table
def print_inventory(inventory):
    console = Console()
    
    # Create a table with headers
    table = Table(show_header=True, header_style="bright_blue")
    table.add_column("Product Name", style="dim", width=20)
    table.add_column("Quantity", justify="right", width=10)
    table.add_column("Buy Price", justify="right", width=15)
    table.add_column("Expiration Date", justify="right", width=15)

    # Populate the table with inventory data
    for item in inventory:
        table.add_row(
            item['product_name'],
            str(item['quantity']),
            f"{item['buy_price']:.2f}",
            item['expiration_date']
        )

    # Print the table using the rich library
    console.print(table)