import csv
import os

# Define the path to the CSV file where the purchased products are stored
bought_path = os.path.join(os.getcwd(), 'data', 'bought.csv')

# Function to add a new product purchase record
def buy_product(product_name, buy_date, buy_price, expiration_date):
    # Open the CSV file for reading
    with open(bought_path, 'r') as csv_file:
        # Create a CSV reader
        reader = csv.DictReader(csv_file)
        # Read the existing data into a list
        data = list(reader)
    
    # Generate a new unique ID for the product purchase
    if len(data) == 0:
        new_id = 0
    else:
        new_id = int(data[len(data)-1]['id']) + 1

    # Create a new record for the purchased product
    new_record = {
        'id': new_id,
        'product_name': product_name.lower(),
        'buy_date': buy_date,
        'buy_price': buy_price,
        'expiration_date': expiration_date
    }

    # Add the new record to the data list
    data.append(new_record)

    # Define the field names for the CSV
    fieldnames = ['id', 'product_name', 'buy_date', 'buy_price', 'expiration_date']

    # Open the CSV file for writing
    with open(bought_path, 'w', newline='') as csv_file:
        # Create a CSV writer
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # Write the CSV header
        writer.writeheader()
        # Write all the data records to the CSV
        writer.writerows(data)
    
    # Print a confirmation message
    print('Ok')

