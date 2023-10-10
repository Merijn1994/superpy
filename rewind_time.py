from datetime import datetime, timedelta
import os

def rewind_time(num_days):
    # Check if num_days has a value greater than 0
    if num_days <= 0:
        print('Please enter a value larger than 0')
        return None

    # Get the path to the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the relative path to the time.txt file
    time_path = os.path.join(script_dir, 'data', 'time.txt')

    # Read the current date stored in the txt file
    with open(time_path, 'r') as txt:
        current_date_str = txt.read().strip()
        current_date = datetime.strptime(current_date_str, '%Y-%m-%d')
    
    rewind_date = current_date - timedelta(days=num_days)
    
    # Check if the rewound date is before today's date
    if rewind_date.date() < datetime.today().date():
        print("Please do not rewind time below today's date")
    else:
        with open(time_path, 'w') as txt:
            txt.write(rewind_date.strftime('%Y-%m-%d'))
    print('Ok')