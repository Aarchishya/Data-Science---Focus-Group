# Dictionaries are unordered, mutable collections of key-value pairs. Each key must be unique, and values can be of any data type.
student = {
    "name": "Alice",
    "age": 20,
    "grades": [88, 92, 95]
}

# Use keys to access values.
print(student["name"])  # "Alice"

# Getting Values: Use the get() method to access values safely.
print(student.get("age"))          # 20
print(student.get("gender", "N/A"))  # "N/A" (default value if key not found)

# Adding/Updating: Assign a value to a key.
student["major"] = "Computer Science"  # Adds a new key-value pair
student["age"] = 21                    # Updates the value of "age"

# Removing: Remove key-value pairs using del or pop().
del student["grades"]
age = student.pop("age")

info = {"name": "Bob", "age": 25}
info["city"] = "New York"
print(info)  # {"name": "Bob", "age": 25, "city": "New York"}

