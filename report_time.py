def report_time():
    with open('time.txt', 'r') as txt:
        date = txt.read()
        print(date)
        return date