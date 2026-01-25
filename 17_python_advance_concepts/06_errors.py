# while True:
#     try:
#         num1 = int(input("Enter first number: "))
#         num2 = int(input("Enter second number: "))
#         result = num1 / num2
#         print(f"The result of {num1} divided by {num2} is {result}")
#     except ValueError:
#         print("Invalid input. Please enter numeric values.")
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = num1 / num2

if num2 == 0:
    raise ZeroDivisionError("Error: Division by zero is not allowed.")

print(f"The result of {num1} divided by {num2} is {result}")
