# There are two types of modules in python
# 1. Built-in modules
# 2. External modules

import math
import myModule
import requests

print(math.sqrt(16))  # Output: 4.0
myModule.hello()  # Output: Hello from myModule!
r = requests.get("https://google.com")
print(r.text)
