from datetime import timedelta, date


# Changes today if there is a positive date offset given.
# Give back the new today
def today(date_offset):

    # Set today to today.
    today = date.today()
    # Changes today using timedelta.
    changed_date = str(today + timedelta(days=date_offset))
    print(f'The date of today is: {changed_date}')
    # Writes today to a text file.
    with open('today.txt', 'w') as today_writer:
        today_writer.write(changed_date)
    today_writer.close()
    return changed_date
