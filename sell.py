import csv
from datetime import datetime
import os

BOUGHT_FILE_PATH = os.path.join(os.getcwd(), 'data', 'bought.csv')
SOLD_FILE_PATH = os.path.join(os.getcwd(), 'data', 'sold.csv')

# Create a set to keep track of sold products
sold_products = set()

def sell_product(product_name, price, sell_date_str):
    global sold_products  # Access the global set of sold products

    # Check if the product has already been sold
    if product_name in sold_products:
        print(f"Product '{product_name}' has already been sold.")
        return

    # Open the bought.csv and sold.csv files
    with open(BOUGHT_FILE_PATH, 'r') as bought_file, open(SOLD_FILE_PATH, 'a', newline='') as sold_file:
        # Create CSV reader and writer objects
        bought_reader = csv.DictReader(bought_file)
        sold_writer = csv.writer(sold_file)

        # Initialize variables to keep track of the oldest matching row in bought.csv
        oldest_row = None
        oldest_date = datetime.max
        expiration_date = None  # Initialize expiration_date outside the loop

        # Iterate over each row in bought.csv
        for bought_row in bought_reader:
            if bought_row['product_name'] == product_name:
                buy_date = datetime.strptime(bought_row['buy_date'], '%Y-%m-%d')
                if buy_date < oldest_date:
                    # Check if the bought_id is already in sold.csv
                    with open(SOLD_FILE_PATH, 'r') as sold_file_check:
                        sold_reader_check = csv.DictReader(sold_file_check)
                        found_in_sold = False
                        for sold_row_check in sold_reader_check:
                            if sold_row_check['bought_id'] == bought_row['id']:
                                found_in_sold = True
                                break
                    if not found_in_sold:
                        oldest_row = bought_row
                        oldest_date = buy_date
                        expiration_date = datetime.strptime(bought_row['expiration_date'], '%Y-%m-%d')

        # If there was no matching row in bought.csv, print an error message and return
        if oldest_row is None:
            print("Desired item not in stock")
            return

        # Parse the sell_date_str to a datetime object for validation
        sell_date = datetime.strptime(sell_date_str, '%Y-%m-%d')

        # Check the validity of the sell date
        if sell_date < oldest_date:
            print(f"Sell date '{sell_date.strftime('%Y-%m-%d')}' is before the buy date of '{oldest_date.strftime('%Y-%m-%d')}' for product '{product_name}'.")
            return
        elif sell_date > expiration_date:
            print(f"Product '{product_name}' with a buy date of '{oldest_date.strftime('%Y-%m-%d')}' has expired and cannot be sold.")
            return

        # Add the sold product to the set of sold products
        sold_products.add(product_name)

        # Calculate the next ID based on the number of rows in 'sold.csv'
        num_rows = sum(1 for _ in csv.reader(open(SOLD_FILE_PATH, 'r'))) - 1

        # Write a new row to sold.csv with the new ID, bought_id, sell date, and sell price
        sold_writer.writerow([num_rows, oldest_row['id'], sell_date.strftime('%Y-%m-%d'), price])

        print('Ok')
