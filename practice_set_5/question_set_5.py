student = {"name": "John", "age": 20, "grade": "A"}

print(student["name"])

student["grade"] = "A+"

student["city"] = "Delhi"

print(student)

friends = {"Rupayan": "9903891234", "Ankit": "9876543210", "Sonal": "9123456780"}

print(friends.keys())
print(friends.values())

for friend in friends.items():
    print(friend)
