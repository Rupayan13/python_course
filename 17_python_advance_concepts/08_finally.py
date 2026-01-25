def divide(num1, num2):
    try:
        result = num1 / num2
        return result

    except Exception as e:
        return f"An unexpected error occurred: {e}"

    # This is always executed
    finally:
        print("Execution of the try-except block is complete.")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(divide(num1, num2))
