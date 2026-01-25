def sum(*args):
    # It will create a tuple of all the arguments passed
    print(args)
    total = 0
    for num in args:
        total += num
    return total


result = sum(1, 2, 3, 4, 5)
print(f"The sum of the arguments is: {result}")
