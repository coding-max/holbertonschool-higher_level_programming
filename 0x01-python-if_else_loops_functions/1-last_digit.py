#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d} ".format(number), end='')

aux = number
if number < 0:
    aux = -number

last_digit = aux % 10
if number < 0:
    last_digit = -last_digit

if last_digit == 0:
    print("is {:d} and is 0".format(last_digit))
elif last_digit > 5:
    print("is {:d} and is greater than 5".format(last_digit))
else:
    print("is {:d} and is less than 6 and not 0".format(last_digit))
