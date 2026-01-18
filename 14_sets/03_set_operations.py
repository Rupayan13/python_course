a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

c = a.union(b)  # Union will combine all unique elements from both sets
print(c)

d = a.intersection(
    b
)  # Intersection will give only the elements that are present in both sets
print(d)
