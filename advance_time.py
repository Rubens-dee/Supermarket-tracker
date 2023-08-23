from argparse import ArgumentTypeError
import today


# Change today if the value is correct
def advance_time(value):
    value = int(value)
    try:
        # Check if the given value is positive
        if value < 0:
            raise ArgumentTypeError('{} is not a positive integer, '
                                    'you can only trave in the future'.format(value))
        # The value is correct and pass it to the module "today"
        else:
            today.today(value)
    # Gives an error if the value is not an integer
    except ValueError:
        raise ArgumentTypeError("{} is not an integer".format(value))
    return value
