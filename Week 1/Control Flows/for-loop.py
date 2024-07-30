# The for loop in Python is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each element in the sequence.

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# The range() function generates a sequence of numbers, which is often used with for loops.

# Prints numbers from 0 to 4
for i in range(5):
    print(i)

# Prints numbers from 1 to 5
for i in range(1, 6):
    print(i)

# Prints every second number from 0 to 10
for i in range(0, 11, 2):
    print(i)

# Iterating Over Strings:
word = "hello"
for char in word:
    print(char)

# Nested Loops:

# Printing a 3x3 grid of numbers
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()

# break: Exits the loop prematurely
for number in range(1, 11):
    if number == 5:
        break
    print(number)  # Prints 1 to 4

# continue: Skips the rest of the current loop iteration and moves to the next one
for number in range(1, 6):
    if number == 3:
        continue
    print(number)  # Prints 1, 2, 4, 5

# Eg 2
for number in range(1, 6):
    if number == 3:
        break
    print(number)
else:
    print("Loop completed")  # This will not be printed because the loop is terminated by break
