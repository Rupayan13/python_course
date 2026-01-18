def sum(a, b):
    print("Adding", a, "and", b)
    c = a + b
    global z  # Declare z as global to modify the global variable
    z = 0
    return c


z = 8  # this z is a global variable
print(z)
print(sum(5, 5))
print(z)  # z is now modified to 0
