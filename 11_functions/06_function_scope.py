def sum(a, b):  # a, b are parameters and they are local to this function
    c = a + b
    # c is also a local variable
    z = 1  # here z is a local variable, it will not modify the value of z outside this function
    return c


z = 8  # this z is a global variable

print(z)
print(sum(5, 5))
print(z)  # z remains unchanged
