from datetime import datetime, timedelta, date


# Adjust the offset date with the given amount of days in future or past
def offset_date(date_offset):
    with open('today.txt', 'r') as today_input:
        date_now = today_input.read()
        date_now = datetime.strptime(date_now, '%Y-%m-%d').date()
        today_input.close()
    # Checks if today is adjusted by the timemachine
    if date_now > date.today():
        offset_date = str(date_now + timedelta(days=date_offset))
        write_offset_date(offset_date)
    else:
        date_now = date.today()
        offset_date = str(date_now + timedelta(days=date_offset))
        write_offset_date(offset_date)
    return offset_date


def write_offset_date(offset_date):
    with open('offset_date.txt', 'w') as file:
        file.write(offset_date)
        file.close()
