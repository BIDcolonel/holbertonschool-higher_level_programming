#!/usr/bin/python3

def fizzbuzz():
    verdict = ""
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            verdict += "FizzBuzz "
        elif index % 3 == 0:
            verdict += "Fizz "
        elif index % 5 == 0:
            verdict += "Buzz "
        else:
            verdict += str(index) + " "

    print(verdict, end="")
