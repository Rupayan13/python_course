# Write a program that counts how many vowels are in a given string.

sentence = "Coding in python is fun."
sum = 0
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
for char in sentence:
    if char in vowels:
        sum += 1
print(f"There are {sum} vowels in the sentence.")

# Take a user input string and check if it is a palindrome (same forwards and backwards)

string = input("Enter a string: ")
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
