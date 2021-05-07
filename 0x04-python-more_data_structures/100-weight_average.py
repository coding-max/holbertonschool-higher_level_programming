#!/usr/bin/python3
def weight_average(my_list=[]):
    "returns the weighted average of all integers tuple (<score>, <weight>)"

    if len(my_list) == 0:
        return (0)
    total = div = 0
    for touple in my_list:
        total += touple[0] * touple[1]
        div += touple[1]
    return (total / div)
