#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    "prints x elements of a list"
    i = pichu = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            pichu += 1
        except:
            continue
    print()
    return pichu
