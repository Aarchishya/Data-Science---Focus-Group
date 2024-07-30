# Tuples are ordered, immutable collections of elements. Once created, the elements cannot be modified.
coordinates = (10, 20)
person = ("Alice", 30, "Engineer")

# Indexing and Slicing: Similar to lists
print(coordinates[0])   # 10
print(person[:2])       # ("Alice", 30)

# Assigning tuple elements to variables.
x, y = coordinates
name, age, profession = person

# Immutability : Tuples cannot be changed after creation, which makes them useful for fixed collections of data.
# However, they can contain mutable elements like lists.


