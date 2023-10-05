#!/usr/bin/python3

def roman_to_int(roman_string):
    romanDictionary = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0

    if not roman_string or not isinstance(roman_string, str):
        return 0

    previousValue = 0

    for numeral in roman_string:
        currentValue = romanDictionary.get(numeral, 0)
        if currentValue > previousValue:
            result += currentValue - 2 * previousValue
        else:
            result += currentValue
        previousValue = currentValue
    return result
