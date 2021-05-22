#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these chars: '.' '?' ':'"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    new_text = ""
    jump = False
    for char in text:
        if jump:
            jump = False
            continue
        new_text += char
        if char in ['.', '?', ':']:
            new_text += "\n\n"
            jump = True
    print(new_text, end='')
