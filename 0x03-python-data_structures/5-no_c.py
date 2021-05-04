#!/usr/bin/python3
def no_c(my_string):
    "removes all characters c and C from a string"

    "new string to return"
    no_c_string = ""
    for i in range(len(my_string)):
        "append if the char is not 'c' or 'C'"
        if my_string[i] != 'c' and my_string[i] != 'C':
            no_c_string += my_string[i]
    return (no_c_string)
