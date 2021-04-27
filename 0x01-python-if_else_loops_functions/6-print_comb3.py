#!/usr/bin/python3
for tens in range(0, 10):
    for ones in range(tens + 1, 10):
        print("{}{}, ".format(tens, ones), end='')
print("89")
