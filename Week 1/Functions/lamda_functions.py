# Lambda functions, also known as anonymous functions, are small, unnamed functions defined using the lambda keyword. They are limited to a single expression and are typically used for short, simple operations.

# Regular function
def add(x, y):
    return x + y

# Lambda function
add_lambda = lambda x, y: x + y

print(add_lambda(2, 3))  # Output: 5

# Use Cases:
# Lambda functions are often used as arguments to higher-order functions that take other functions as input, such as map(), filter(), and sorted().

# Example with map():
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Example with filter():
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4]

# Example with sorted():
points = [(1, 2), (3, 1), (5, 7), (2, 2)]
sorted_points = sorted(points, key=lambda x: x[1])
print(sorted_points)  # Output: [(3, 1), (1, 2), (2, 2), (5, 7)]


