#!/usr/bin/python3

def remove_char_at(str, n):
    newString = str if n < 0 else str[:n] + str[n+1:]
    return newString
