#!/usr/bin/python3
a = 89
b = 10
a, b = (b, a) if isinstance(a, int) and isinstance(b, int) else (b, a)
print("a={:d} - b={:d}".format(a, b))
