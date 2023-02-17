import os
import csv

parent_dir = os.path.dirname(__file__)
bought_path = os.path.join(parent_dir, 'csv data\\bought.csv')
sold_path = os.path.join(parent_dir, 'csv data\\sold.csv')
inventory_output = []

# Function for the report inventory command
def report_inventory():
# Read the bought.csv file and put data in dictionaries nested in a list
    with open(bought_path, 'r', newline='') as csv_file:
        reader1 = csv.DictReader(csv_file)
        bought_data_list = list(reader1)

    with open(sold_path, 'r', newline='') as csv_file:
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
    return inventory_output