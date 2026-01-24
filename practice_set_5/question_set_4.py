my_set = {1, 2, 3, 3, 4}

print(my_set)  # Output: {1, 2, 3, 4} - duplicates are removed

my_set.add(5)
print(my_set)

my_set.remove(2)
print(my_set)

# check if 4 is present in the my_set
print(4 in my_set)  # Output: True

a = {1, 2, 3}

b = {3, 4, 5}

# Union of sets
print(a.union(b))

# Intersection of sets
print(a.intersection(b))

# Difference of sets
print(a.difference(b))
