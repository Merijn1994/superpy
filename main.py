# Imports
import argparse
import os
import csv
from datetime import date

# Declaring variables
parent_dir = os.path.dirname(__file__)
inventory_file = 'inventory.csv'
sold_file = 'sold.csv'
column_headers = []
rows = []

def read_csv_file(file):
    path_file = os.path.join(parent_dir, file)

    with open(path_file) as csv_file:
        reader = csv.reader(csv_file)

        column_headers = next(reader)

        for row in reader:
            rows.append(row)
    print('The column headers: ' + str(column_headers))
    print('The items in stock: ' + str(rows))    

def main():
    pass


if __name__ == "__main__":
    main()
    read_csv_file(inventory_file)
