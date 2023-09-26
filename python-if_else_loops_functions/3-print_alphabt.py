#!/usr/bin/python3
str = ""
for letter in range(97, 123):
    if chr(letter) not in ['q', 'e']:
        str += chr(letter)

print("{}".format(str), end="")
