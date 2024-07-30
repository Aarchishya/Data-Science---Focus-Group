# The if statement is used to execute a block of code if a specified condition is true. It can be followed by optional elif (else if) and else blocks to handle multiple conditions and default cases.

temperature = 30

if temperature > 30:
    print("It's a hot day.")
elif temperature == 30:
    print("It's a warm day.")
else:
    print("It's a cool day.")

# Example with Logical Operators:
age = 18
has_permission = True

if age >= 18 and has_permission:
    print("You are allowed to enter.")
else:
    print("You are not allowed to enter.")
