from datetime import datetime
import os

# Get the path to the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to the time.txt file
time_path = os.path.join(script_dir, 'data', 'time.txt')

def report_time():
    # Read the current date stored in the txt file
    with open(time_path, 'r') as txt:
        current_date_str = txt.read().strip()
        current_date = datetime.strptime(current_date_str, '%Y-%m-%d')

    # Print the current date
    return current_date.strftime('%Y-%m-%d')