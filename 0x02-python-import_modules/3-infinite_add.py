#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0

    length = len(sys.argv) - 1
    if (length == 0):
        print(total)
    else:
        for i in range(1, len(sys.argv)):
            total += int(sys.argv[i])
        print(total)
