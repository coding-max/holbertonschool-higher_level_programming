#!/usr/bin/python3
    "returns a key with the biggest integer value"

    biggest_value = 0
    biggest_key = None
    for key, value in a_dictionary.items():
        if value > biggest_value:
            biggest_value = value
            biggest_key = key
    return biggest_key
