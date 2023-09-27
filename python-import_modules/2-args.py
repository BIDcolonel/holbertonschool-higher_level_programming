#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    numberOfArguments = len(arguments)

    if numberOfArguments == 0:
        print("0 arguments.")
    else:
        severalArguments = 's' if numberOfArguments > 1 else ''
        print("{} argument{}:".format(numberOfArguments, severalArguments))

    for index, arg in enumerate(arguments, 1):
        print("{}: {}".format(index, arg))
