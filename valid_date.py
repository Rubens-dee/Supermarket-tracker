from datetime import datetime


# Check if the given date is a valid date (YYYY-MM-DD)
def validate(date_string):
    try:
        date_string = datetime.strptime(date_string, '%Y-%m-%d').date()
        return date_string
    # If date is not valid an error will be raised
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
        # Ends programs
        raise SystemExit()


# Check if the given date is a valid date (YYYY-MM)
def validate_year_month(date_string):
    try:
        date_string = datetime.strptime(date_string, '%Y-%m').date()
        date_string = datetime.strftime(date_string, '%Y-%m')
        return date_string
        # If date is not valid an error will be raised
    except ValueError:
        print("Incorrect data format, should be YYYY-MM")
        # Ends programs
        raise SystemExit()
