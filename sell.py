import csv
import os

parent_dir = os.path.dirname(__file__)
bought_path = os.path.join(parent_dir, 'csv data\\bought.csv')
sold_path = os.path.join(parent_dir, 'csv data\\sold.csv')

def sell_product():
    with open(sold_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        sold_data = list(reader)

    new_id = int(sold_data[len(sold_data)-1]['id']) + 1

    with open(bought_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        bought_data = list(reader)