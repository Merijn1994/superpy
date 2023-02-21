# Imports
import argparse
from datetime import datetime

from buy import buy_product
from sell import sell_product
from report_time import report_time
from advance_time import advance_time
from report_inventory import get_inventory, print_inventory


# Initialize the date
today = datetime.today()
with open('time.txt', 'r') as txt:
    initial_date = datetime.strptime(txt.read(),'%Y-%m-%d')

    if today != initial_date:
        with open('time.txt', 'w') as txt:
            txt.write(datetime.strftime(today, '%Y-%m-%d'))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', help='The command to run', choices=['report_inventory'])
    args = parser.parse_args()

    if args.command == 'report_inventory':
        inventory = get_inventory()
        print_inventory(inventory)

if __name__ == "__main__":
    main()
