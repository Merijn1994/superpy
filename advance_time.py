def advance_time(days_to_advance):
    with open('time.txt', 'r') as txt:
        time = txt.read()
        day = int(time[-2:len(time)])
        day += days_to_advance
        new_time = time.replace(time[-2:len(time)], str(day))
    with open('time.txt', 'w') as txt:
        txt.write(new_time)
    print('Ok')