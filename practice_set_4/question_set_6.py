def increment(counter):
    counter += 1


counter = 0
print(counter)  # Output: 0
increment(counter)
print(counter)  # Output: 0


def multiply(a, b):
    """It multiplies two numbers and returns the result"""
    return a * b


def help(fun):
    print(fun.__doc__)


help(multiply)
