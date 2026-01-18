import math
import requests

def square_root(x):
    return math.sqrt(x)


print(square_root(144))

print(math.radians(math.sin(90)))

print(requests.get("https://api.github.com").text)
