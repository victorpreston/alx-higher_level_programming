#!/usr/bin/python3
"""Defining a function text_indentation"""


def text_indentation(text):
    """Prints Text with 2 lines after ['.', '?', and ':'.]

    Args:
        text (string): Printed Text.
    Raises:
        TypeError: Text not string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
