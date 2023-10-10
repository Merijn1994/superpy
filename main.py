from rich.console import Console
from rich.syntax import Syntax
from create_parser import create_parser

from buy import buy_product
from sell import sell_product
from report_time import report_time
from advance_time import advance_time
from reset_time import reset_time
from rewind_time import rewind_time
from report_inventory import get_inventory, print_inventory

# Declaring variables
console = Console() # initialize rich console
parser = create_parser() # create the command line parser

def main():
    args = parser.parse_args() # parse the command line arguments

    # check which command was entered and execute the appropriate function
    if args.command == 'buy':
        buy_product(args.product_name, report_time(), args.price, args.expiration_date)
    elif args.command == 'sell':
        sell_product(args.product_name, args.price, report_time())
    elif args.command == 'report_time':
        console.print(report_time())
    elif args.command == 'report_inventory':
        print_inventory(get_inventory())
    elif args.command == 'advance_time':
        advance_time(args.days)
    elif args.command == 'rewind_time':
        rewind_time(args.days)
    elif args.command == 'reset_time':
        reset_time()
    else:
        syntax = Syntax('''Usage: python <script.py> <command> [<args>]
        
        Commands:
            buy --product-name [name] --price [price] --expiration-date [expiration date]   Buy a product
            sell --product-name [name] --price [price]                                      Sell a product
            report_inventory [time]                                                         Get the state of inventory based on the given time
            report_time                                                                     Get the current time
            advance_time [days]                                                             Advance the current time by a given number of days
            rewind_time [days]                                                              Rewind the current time by a given number of days
            reset_time                                                                      Reset the current time to the current date''',
                        "bash",
                            theme="monokai")

        console.print(syntax)

if __name__ == "__main__":
    main()
