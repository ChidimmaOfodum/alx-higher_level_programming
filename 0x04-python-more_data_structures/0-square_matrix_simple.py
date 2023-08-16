#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result =  list(map(lambda x: list(map(lambda y: y* y, x)), matrix))
    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
