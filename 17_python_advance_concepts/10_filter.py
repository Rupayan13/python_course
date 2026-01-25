# def is_greater_than_9(num):
#     if num > 9:
#         return True
#     else:
#         return False


numbers = [1, 2, 3, 45, 4, 21]
filtered_numbers = list(filter(lambda num: num > 9, numbers))
print(filtered_numbers)
