# Imports
import argparse
import os
import csv
from datetime import date

# Declaring variables
parent_dir = os.path.dirname(__file__)
bought_file = 'bought.csv'
sold_file = 'sold.csv'
inventory_output = []

# Initialize the date
today = date.today()
with open('time.txt', 'w') as f:
    f.write(str(today))

# Function for the report inventory command
def report_inventory(file1, file2):
    path_file1 = os.path.join(parent_dir, file1)
    path_file2 = os.path.join(parent_dir, file2)
# Read the bought.csv file and put data in dictionaries nested in a list
    with open(path_file1, 'r', newline='') as csv_file:
        reader1 = csv.DictReader(csv_file)
        bought_data_list = list(reader1)

    with open(path_file2, 'r', newline='') as csv_file:
        reader2 = csv.DictReader(csv_file)
        sold_data_list = list(reader2)

    for bought_data in bought_data_list:
        for sold_data in sold_data_list:
            # Iterate through inventory List and find duplicate item  
            inventory = next(
                (
                    item for item in inventory_output if
                    item["Product Name"] == bought_data['product_name'] and
                    item["Buy Price"] == bought_data['buy_price'] and
                    item["Expiration Date"] == bought_data['expiration_date']
                ), None
            )

            # Add stock to duplicate or add new product
            if inventory and bought_data['id'] != sold_data['bought_id']:
                inventory['Stock'] += 1
            elif inventory is None and bought_data['id'] != sold_data['bought_id']:
                inventory_output.append(
                    {   
                        'Product Name': bought_data['product_name'],
                        'Stock': 1,
                        'Buy Price': bought_data['buy_price'],
                        'Expiration Date': bought_data['expiration_date']
                    })
            print(inventory_output)

def advance_time(days_to_advance):
    with open('time.txt', 'r') as f:
        time = f.read()
        day = int(time[-2:len(time)])
        day += days_to_advance
        new_time = time.replace(time[-2:len(time)], str(day))
    with open('time.txt', 'w') as f:
        f.write(new_time)




# def write_csv_file(file):
#     path_file = os.path.join(parent_dir, file)

#     with open(path_file, 'w', newline='') as csv_file:
#         writer = csv.writer(csv_file)

def main():
    pass

if __name__ == "__main__":
    main()
    report_inventory(bought_file, sold_file)
    # write_csv_file(bought_file)
    advance_time(2)
