#!/usr/bin/python3
def weight_average(my_list=[]):
    if (len(my_list) == 0):
        return 0
    n = total = 0
    for i in my_list:
        first, second = i
        n += second
        total += (first * second)
    return total / n
