def very_slow_func():
    print("Something...")
    print("Something...")
    print("Something...")
    print("Something...")
    return 70


# a = very_slow_func()
# if (a := very_slow_func()) > 10:
#     print(a)
# else:
#     print("Less than 10")

while data := input("Enter an alphabet:"):
    print(f"You entered: {data}")
    if data.lower() == "q":
        break
