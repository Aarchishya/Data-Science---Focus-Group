# Strings are sequences of characters, enclosed in single, double, or triple quotes. They are used to store text data.

single_quote_str = 'Hello'
double_quote_str = "World"
triple_quote_str = """This is a
multi-line string"""

# Concatenation: Joining two or more strings using the + operator.
greeting = "Hello, " + "Alice!"

# Repetition: Repeating a string multiple times using the * operator.
repeated_str = "Ha" * 3  # "HaHaHa"

# Indexing: Accessing individual characters in a string using indices (starts at 0).
first_letter = greeting[0]  # 'H'

# Slicing: Extracting a substring using the slice notation [start:stop:step].
substring = greeting[0:5]  # 'Hello'

# String Length: Using the len() function to get the length of a string.
length = len(greeting)  # 7

# upper(): Converts all characters to uppercase.
print(greeting.upper())  # "HELLO, ALICE!"

# lower(): Converts all characters to lowercase.
print(greeting.lower())  # "hello, alice!"

# replace(old, new): Replaces occurrences of a substring with another substring.
print(greeting.replace("Alice", "Bob"))  # "Hello, Bob!"

# split(delimiter): Splits the string into a list of substrings based on the specified delimiter.
words = greeting.split(", ")  # ['Hello', 'Alice!']
print(words);