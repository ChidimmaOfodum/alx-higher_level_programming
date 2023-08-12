#!/usr/bin/python3
import sys

length = len(sys.argv) - 1
if (length == 0):
    arguments = "arguments."
else:
    arguments = "argument:" if length == 1 else "arguments:"

print("{:d} {}".format(length, arguments))

if length > 0:
    for i in range(1, length + 1):
        print("{}: {}".format(i, sys.argv[i]))
