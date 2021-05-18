#!/usr/bin/python3
def safe_print_integer_err(value):
    "prints an integer with error message"
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as err:
        print("Exception: {}".format(err))
        return False
