coordinates = (10, 20)
print(coordinates[0])
print(coordinates[1])

# coordinates[0] = 50  # This will raise a TypeError because tuples are immutable

coordinates_list = list(coordinates)
coordinates_list[0] = 50
coordinates = tuple(coordinates_list)
print(coordinates)
