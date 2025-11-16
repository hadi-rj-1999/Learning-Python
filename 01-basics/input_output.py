# ---------------------------------------------------
# Python Input & Output
# ---------------------------------------------------
# This file explains how to use input() for user input
# and print() for displaying output in Python.
# ---------------------------------------------------

# ---------------------------------------------
# BASIC OUTPUT
# ---------------------------------------------
print("Hello, Python!")
print("This is an example of output.")

# You can print multiple values:
name = "Hadi"
age = 26
print("Name:", name, "| Age:", age)

# Using 'sep' and 'end' parameters:
print("A", "B", "C", sep="-")    # A-B-C
print("Hello", end=" ")          # does not create a new line
print("World")                   # continues from previous line

# ---------------------------------------------
# BASIC INPUT
# ---------------------------------------------
# input() always returns a string

# Uncomment these lines if you want to test input in runtime:
# user_name = input("Enter your name: ")
# print("Hello", user_name)

# ---------------------------------------------
# INPUT CONVERSION (Casting)
# ---------------------------------------------
# Since input() returns a string, convert it manually:

# Example of converting user input to integer:
# number = int(input("Enter a number: "))
# print("Number + 10 =", number + 10)

# Example of converting to float:
# price = float(input("Enter a price: "))
# print("Price * 2 =", price * 2)

# ---------------------------------------------
# READING MULTIPLE INPUTS
# ---------------------------------------------
# Example: split() to get multiple values in one line
# a, b = input("Enter two numbers: ").split()
# print(a, b)

# With type conversion:
# x, y = map(int, input("Enter two integers: ").split())
# print("Sum:", x + y)

# ---------------------------------------------
# FORMATTED OUTPUT
# ---------------------------------------------
# Using f-strings (recommended):
user = "Hadi"
score = 95.5
print(f"User: {user} | Score: {score}")

# Using format():
print("User: {} | Score: {}".format(user, score))

# ---------------------------------------------
# MULTILINE OUTPUT
# ---------------------------------------------
print("""
This is a multiline text.
Works with triple quotes.
""")

# ---------------------------------------------
# SUMMARY:
# - print() outputs data
# - input() receives data as string
# - cast input using int(), float(), etc.
# - f-strings are best for formatting output
