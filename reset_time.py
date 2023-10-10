from datetime import datetime
import os

# Get the path to the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to the time.txt file
time_path = os.path.join(script_dir, 'data', 'time.txt')

# Get the current date
current_date = datetime.today()

def reset_time():
	# Write the current date to the time.txt file
	with open(time_path, 'w') as txt:
		txt.write(current_date.strftime('%Y-%m-%d'))
	
	print('Time reset to current date')