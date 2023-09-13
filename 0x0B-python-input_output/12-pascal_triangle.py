#!/usr/bin/python3

def pascal_triangle(n):
    """List of integers representing Pascal triangle"""
    result = []
    if (n <= 0):
        return result

    for i in range(n):
        inner = []
        for j in range(i + 1):
            if (j == 0 or j == i):
                inner.append(1)
            else:
                x = result[i - 1][j] + result[i - 1][j-1]
                inner.append(x)
        result.append(inner)
    return result
