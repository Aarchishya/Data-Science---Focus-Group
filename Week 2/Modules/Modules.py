# Modules are files containing Python code that can define functions, classes, and variables.

# 1) Built-in Modules
# Python's standard library includes many useful modules. You can import and use these modules in your code.

import math
print(math.sqrt(16))  # Output: 4.0
print(math.pi)        # Output: 3.141592653589793

# 2. Installing Third-Party Modules with pip
# For eg :pip install requests
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # Output: 200
print(response.json())       # Output: JSON response from the API

# Creating a Custom Module:
# A module is simply a Python file with a .py extension. You can create your own modules to organize your code
# module.py used in main.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b



