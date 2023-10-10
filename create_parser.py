# Imports
import argparse

def create_parser():
	# Create the parser object
	parser = argparse.ArgumentParser()

	# Create subparsers for different commands
	subparsers = parser.add_subparsers(dest='command')

	# Create parser for the "buy" command
	buy_parser = subparsers.add_parser('buy', help='Command to buy a product')
	buy_parser.add_argument('--product-name', type=str, help='Name of the product', required=True)
	buy_parser.add_argument('--price', type=str, help='Price of the product', required=True)
	buy_parser.add_argument('--expiration-date', type=str, help='Expiration date of the product', required=True)

	# Create parser for the "sell" command
	sell_parser = subparsers.add_parser('sell', help='Command to sell a product')
	sell_parser.add_argument('--product-name', type=str, help='Name of the product', required=True)
	sell_parser.add_argument('--price', type=str, help='Price of the product', required=True)

	# Create parser for the "report_inventory" command
	subparsers.add_parser('report_inventory', help='Command to show the inventory for the set date')

	# Create parser for the "report_time" command
	subparsers.add_parser('report_time', help='Command to show the current set date')

	# Create parser for the "advance_time" command
	advance_time_parser = subparsers.add_parser('advance_time', help='Command to advance the current set time by an amount of days')
	advance_time_parser.add_argument('days', type=int, help='Number of days to advance the time')

	# Create parser for the "rewind_time" command
	rewind_time_parser = subparsers.add_parser('rewind_time', help='Command to rewind the current set time by an amount of days')
	rewind_time_parser.add_argument('days', type=int, help='Number of days to rewind the time')

	# Create parser for the "reset_time" command
	subparsers.add_parser('reset_time', help='Command to reset the current time to the current date')
		
	return parser

