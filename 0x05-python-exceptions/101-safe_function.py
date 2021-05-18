#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct(*args)
    except (TypeError, ValueError, IndexError, ZeroDivisionError) as error:
        print("Exception: {}".format(error))
        return None
