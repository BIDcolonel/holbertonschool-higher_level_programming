#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":

    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    func = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }

    if operator not in func:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, func[operator](a, b)))
