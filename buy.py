import csv
import os

parent_dir = os.path.dirname(__file__)
bought_path = os.path.join(parent_dir, 'data', 'bought.csv')

def buy_product(product_name, buy_date, buy_price, expiration_date):
    with open(bought_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)
    
    new_id = int(data[len(data)-1]['id']) + 1
    data.append({
        'id': new_id,
        'product_name': product_name,
        'buy_date': buy_date,
        'buy_price': buy_price,
        'expiration_date': expiration_date
    })

    fieldnames = ['id', 'product_name', 'buy_date', 'buy_price', 'expiration_date']

    with open(bought_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(data)

