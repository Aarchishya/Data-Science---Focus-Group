# Lists are ordered, mutable collections of elements. 
# They can store items of different data types and can be modified after creation.

numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed_list = [1, "hello", 3.14, True]

# Indexing: Use indices to access individual elements (0-based).
print(fruits[0])  # "apple"
print(fruits[-1]) # "cherry" (last element)

# Slicing: Extract a portion of the list using [start:stop:step]
print(fruits[1:3]) # ['banana', 'cherry']

# Appending: Add an element to the end of the list.
fruits.append("orange")

# Inserting: Add an element at a specific position.
fruits.insert(1, "mango")

# Removing: Remove elements by value or index.
fruits.remove("banana")  # Removes the first occurrence of "banana"
del fruits[0]            # Removes the first element

colors = ["red", "blue", "green"]
colors.append("yellow")
print(colors)  # ["red", "blue", "green", "yellow"]
colors.sort()
print(colors)  # ["blue", "green", "red", "yellow"]



