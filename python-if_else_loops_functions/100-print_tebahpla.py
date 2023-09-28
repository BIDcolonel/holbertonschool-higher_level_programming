#!/usr/bin/python3

for letter in range(122, 96, -1):
    char = chr(letter)
    if letter % 2:
        char = char.upper()
    print("{}".format(char), end="")
