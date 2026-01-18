def fibonacci(n):
    if n == 1 or n == 0:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(1, 6):
    print(fibonacci(i))


def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


print(safe_divide(10, 2))
print(safe_divide(10, 0))

import my_utils

print(my_utils.is_even(4))  # Output: True
print(my_utils.is_even(5))  # Output: False
