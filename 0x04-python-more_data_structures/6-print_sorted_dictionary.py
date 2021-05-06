#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    "prints a dictionary by ordered keys"

    for i in sorted(a_dictionary.keys()):
        print("{}: {}".format(i, a_dictionary[i]))
