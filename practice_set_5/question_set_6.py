# Write a program that takes a list of numbers and removes all duplicates using a set.
numbers = [5, 2, 9, 1, 7, 5, 2, 9]

uniques = set(numbers)

print(uniques)  # Output: {1, 2, 5, 7, 9} - duplicates are removed

products = {"laptop": 50000, "smartphone": 20000, "tablet": 15000}

# Given a dictionary of products and their prices, find the product with the highest price.

highest_priced_product = ""
highest_price = 0
for price in products:
    if products[price] > highest_price:
        highest_price = products[price]
        highest_priced_product = price

print(
    f"The highest priced product is {highest_priced_product} with a price of {highest_price}."
)


# Write a program that merges two dictionaries into one.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
