#!/usr/bin/python3
"""My list"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """prints the list (sorted)"""
        print(sorted(self))
