#!/usr/bin/python3
for tens in range(0, 9):
    for ones in range(tens + 1, 10):
        if tens != 8:
            print("{}{}, ".format(tens, ones), end='')
print("89")
