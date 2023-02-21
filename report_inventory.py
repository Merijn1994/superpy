import csv
import os
from rich.console import Console
from rich.table import Table

BOUGHT_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'bought.csv'))
SOLD_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'sold.csv'))

def get_inventory():
    bought_items = {}
    with open(BOUGHT_FILE_PATH, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            key = (row['product_name'].lower(), float(row['buy_price']), row['expiration_date'])
            if key not in bought_items:
                bought_items[key] = {
                    'bought_ids': set(),
                    'product_name': row['product_name'].lower(),
                    'buy_price': float(row['buy_price']),
                    'expiration_date': row['expiration_date'],
                    'quantity': 0,
                }
            bought_items[key]['quantity'] += 1
            bought_items[key]['bought_ids'].add(row['id'])

    with open(SOLD_FILE_PATH, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            bought_id = row['bought_id']
            for item in bought_items.values():
                if bought_id in item['bought_ids']:
                    item['quantity'] -= 1

    inventory = []
    for item in bought_items.values():
        if item['quantity'] > 0:
            inventory.append(item)
    return inventory


def print_inventory(inventory):
    console = Console()
    table = Table(show_header=True, header_style="bright_blue")
    table.add_column("Product Name", style="dim", width=20)
    table.add_column("Quantity", justify="right", width=10)
    table.add_column("Buy Price", justify="right", width=15)
    table.add_column("Expiration Date", justify="right", width=15)

    for item in inventory:
        table.add_row(
            item['product_name'],
            str(item['quantity']),
            f"{item['buy_price']:.2f}",
            item['expiration_date']
        )

    console.print(table)