#!/usr/bin/python3
alphabet = ""
for ascii_value in range(97, 123):
    if chr(ascii_value) not in ['q', 'e']:
        alphabet += chr(ascii_value)

print("{}".format(alphabet), end="")
