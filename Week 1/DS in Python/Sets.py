# Sets are unordered collections of unique elements. They are mutable but do not support duplicate entries.
numbers_set = {1, 2, 3, 4}
unique_letters = set("hello")  # {'h', 'e', 'l', 'o'}

# Adding Elements: Use add().
numbers_set.add(5)

# Removing Elements: Use remove() or discard().
numbers_set.remove(1)
numbers_set.discard(2)

# Set Operations: Union, Intersection, Difference, and Symmetric Difference.
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # Union: {1, 2, 3, 4, 5}
print(a & b)  # Intersection: {3}
print(a - b)  # Difference: {1, 2}
print(a ^ b)  # Symmetric Difference: {1, 2, 4, 5}

