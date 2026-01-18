s = {34, 22, 1, 3, 43}

print(s, type(s))

s.add(55)
s.add(100)
print(s)
s.remove(1)
print(s)
# s.remove(422)  # This will raise a KeyError because 422 is not in the set.
s.discard(422)  # This will NOT raise an error even though 422 is not in the set.
print(s)
