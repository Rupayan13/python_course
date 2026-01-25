try:
    a = 345 / 10

except Exception as e:
    print("An error occurred:", e)

# Executed when there is no error in try block
else:
    print("The result is:", a)
