def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))


def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


print(sum_of_digits(1234))
