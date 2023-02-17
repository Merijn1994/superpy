# Imports
import argparse
from datetime import date

from buy import buy_product
from sell import sell_product
from report_inventory import report_inventory
from report_time import report_time
from advance_time import advance_time


# Initialize the date
today = date.today()
with open('time.txt', 'w') as txt:
    txt.write(str(today))

def main():
    pass

if __name__ == "__main__":
    main()
    # report_inventory()
    # buy_product(buy_date = report_time())
    advance_time(5)
    report_time()
