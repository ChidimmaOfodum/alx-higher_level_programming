#!/usr/bin/python3
def weight_average(my_list=[]):
    n = total = 0
    for i in my_list:
        first, second = i
        n += second
        total += (first * second)
    return total / n
