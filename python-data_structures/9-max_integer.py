#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        biggestNumber = my_list[0]
    else:
        biggestNumber = None

    for index in my_list:
        if index > biggestNumber:
            biggestNumber = index
    return (biggestNumber)
