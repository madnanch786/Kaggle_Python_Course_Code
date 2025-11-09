# This course covers the key Python skills you’ll need so you can start using Python for data science.
# The course is ideal for someone with some previous coding experience who wants to add Python to their repertoire.
# (If you're a first-time coder, you are encouraged to check out our Intro to Programming course.)

# We'll start with a brief overview of Python syntax, variable assignment, and arithmetic operators.

# Hello, Python!
# Python was named for the British comedy troupe Monty Python, so we'll make our first Python program a homage to their skit about Spam.

# Try predicting what the following code will do:

spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)

# This program demonstrates variable assignment, conditionals, strings, and arithmetic.

# Variable assignment example:
# spam_amount = 0
# The '=' is the assignment operator.

# No need to declare variables or specify types in Python.

# print(spam_amount)
# Displays the current value of spam_amount on the screen.

# Reassignment example:
# spam_amount = spam_amount + 4
# Adds 4 to the previous value.

# Conditional statement example:
if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam Spam Spam"
print(viking_song)

# The colon (:) starts an indented block.
# Indentation defines which code belongs to the if-statement.

# Strings in Python can be enclosed in single or double quotes.
# Example:
# "But I don't want ANY spam!"

viking_song = "Spam " * spam_amount
print(viking_song)

# The * operator can repeat strings as well as multiply numbers.
# Example: "Spam " * 4 -> "Spam Spam Spam Spam"

# Numbers and arithmetic in Python
spam_amount = 0
# Let's check the type of spam_amount:
print(type(spam_amount))  # int

# Another numeric type in Python is float:
print(type(19.95))  # float

# type() returns the data type of a variable or value.

# Common arithmetic operators:
# a + b -> Addition
# a - b -> Subtraction
# a * b -> Multiplication
# a / b -> True division
# a // b -> Floor division
# a % b -> Modulus
# a ** b -> Exponentiation
# -a -> Negation

print(5 / 2)  # 2.5
print(6 / 2)  # 3.0

# Floor division rounds down:
print(5 // 2)  # 2
print(6 // 2)  # 3

# Order of operations (PEMDAS):
print(8 - 3 + 2)    # 7
print(-3 + 4 * 2)   # 5

# Parentheses can change the evaluation order:
hat_height_cm = 25
my_height_cm = 190
# Without parentheses:
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters =", total_height_meters, "?")

# With parentheses for correct order:
total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters =", total_height_meters)

# Built-in numeric functions:
# min(), max(), abs(), int(), float()

print(min(1, 2, 3))   # 1
print(max(1, 2, 3))   # 3
print(abs(32))        # 32
print(abs(-32))       # 32

# Type conversion examples:
print(float(10))      # 10.0
print(int(3.33))      # 3
print(int('807') + 1) # 808
