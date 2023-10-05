#!/usr/bin/python3

def search_replace(my_list, search, replace):
    newList = []

    for element in my_list:
        if element == search:
            newList.append(replace)
        else:
            newList.append(element)

    return newList
