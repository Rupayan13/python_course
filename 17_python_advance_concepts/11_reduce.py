from functools import reduce

numbers = [1, 2, 3, 4, 5]
#         [3, 3, 4, 5]
#         [6, 4, 5]
#         [10, 5]
#         [15]


def sum(a, b):
    return a + b


result = reduce(sum, numbers)
print(result)
