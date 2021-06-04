====================
TESTS / 1-my_list.py
====================

>>> MyList = __import__("1-my_list").MyList

>>> issubclass(MyList, list)
True
>>> l = MyList()
>>> l.print_sorted()
[]
>>> print(l)
[]
>>> l.print_sorted()
[]
>>> l.append(2)
>>> l.append(7)
>>> l.append(9)
>>> l.append(5)
>>> print(l)
[2, 7, 9, 5]
>>> l.print_sorted()
[2, 5, 7, 9]
>>> l.append(0)
>>> l.append(-3)
>>> print(l)
[2, 7, 9, 5, 0, -3]
>>> l.print_sorted()
[-3, 0, 2, 5, 7, 9]
>>> print(l)
[2, 7, 9, 5, 0, -3]


>>> l = MyList()
>>> print(l)
[]
>>> l.append(-2)
>>> l.append(-7)
>>> l.append(-9)
>>> l.append(-5)
>>> print(l)
[-2, -7, -9, -5]
>>> l.print_sorted()
[-9, -7, -5, -2]
>>> print(l)
[-2, -7, -9, -5]


>>> l.print_sorted(1)
Traceback (most recent call last):
TypeError: print_sorted() takes 1 positional argument but 2 were given
