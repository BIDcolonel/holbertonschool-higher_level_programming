#!/usr/bin/python3
separation = ", "
for index_one in range(9):
    for index_two in range(index_one + 1, 10):
        if index_one == 8 and index_two == 9:
            separation = "\n"
        print("{}{}".format(index_one, index_two), end=separation)
