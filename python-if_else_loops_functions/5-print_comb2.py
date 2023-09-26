#!/usr/bin/python3
separation = ", "
for number in range(0, 100):
    if number == 99:
        separation = "\n"
    print("{:02}".format(number), end=separation)
