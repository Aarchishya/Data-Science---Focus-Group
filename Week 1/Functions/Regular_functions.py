# A function is defined using the def keyword, followed by the function name, parentheses (which may include parameters), and a colon. The function body contains the code to be executed.

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!

# Example with Parameters:
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  # Output: 8

# Example with Default Parameters:
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Output: Hello, Guest!
greet("Alice")   # Output: Hello, Alice!

# Example with Return Value:
def multiply(a, b):
    return a * b

product = multiply(4, 5)
print(product)  # Output: 20

