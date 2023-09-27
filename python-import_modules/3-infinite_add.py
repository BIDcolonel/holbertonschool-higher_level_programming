#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    numberOfArguments = len(arguments)
    result = 0

    if numberOfArguments != 0:
        result = sum(int(arg) for arg in arguments)
    print("{}".format(result))
