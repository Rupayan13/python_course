# Decoraters is a function which takes a function, it creates a wrapper function, then it returns the wrapper function.
def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")

    return wrapper


@decorator
def say_hello():
    print("Hello!")


# f = decorator(say_hello)
# f()

say_hello()
