# ---------------------------------------------------
# Python Conditional Statements - if, elif, else
# ---------------------------------------------------
# Conditional statements are used to make decisions in code.
# They execute different blocks of code based on conditions.
# ---------------------------------------------------

# ---------------------------------------------
# BASIC IF STATEMENT
# ---------------------------------------------
age = 18
if age >= 18:
    print("You are an adult.")
    print("You can vote.")

# ---------------------------------------------
# IF-ELSE STATEMENT
# ---------------------------------------------
temperature = 25
if temperature > 30:
    print("It's hot outside.")
else:
    print("It's not too hot.")

# ---------------------------------------------
# IF-ELIF-ELSE STATEMENT
# ---------------------------------------------
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# ---------------------------------------------
# COMPARISON OPERATORS
# ---------------------------------------------
# == (equal), != (not equal), >, <, >=, <=
x = 10
y = 5

if x == y:
    print("x equals y")
elif x > y:
    print("x is greater than y")
else:
    print("x is less than y")

# ---------------------------------------------
# LOGICAL OPERATORS (and, or, not)
# ---------------------------------------------
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive a car.")
else:
    print("You cannot drive a car.")

# Check if number is between 1 and 100
number = 42
if 1 <= number <= 100:
    print("Number is between 1 and 100")

# Using 'or' operator
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's weekend!")
else:
    print("It's a weekday.")

# Using 'not' operator
is_raining = False
if not is_raining:
    print("No need for an umbrella.")

# ---------------------------------------------
# NESTED IF STATEMENTS
# ---------------------------------------------
num = 15
if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("and it's even")
    else:
        print("and it's odd")
else:
    print("Non-positive number")

# ---------------------------------------------
# TERNARY OPERATOR (Conditional Expression)
# ---------------------------------------------
# Short way to write if-else in one line
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")

# Another example
x = 10
y = 20
max_value = x if x > y else y
print(f"Maximum value: {max_value}")

# ---------------------------------------------
# CHECKING MULTIPLE CONDITIONS
# ---------------------------------------------
username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    print("Login successful")
else:
    print("Invalid credentials")

# ---------------------------------------------
# CHECKING IF VALUE IS IN A LIST
# ---------------------------------------------
fruits = ["apple", "banana", "orange"]
if "banana" in fruits:
    print("Banana is in the list")

if "grape" not in fruits:
    print("Grape is not in the list")

# ---------------------------------------------
# EMPTY CHECK
# ---------------------------------------------
name = ""
if not name:
    print("Name is empty")

my_list = []
if not my_list:
    print("List is empty")

# ---------------------------------------------
# PRACTICAL EXAMPLES
# ---------------------------------------------
# Example 1: Simple calculator
a = 10
b = 5
operation = "+"

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    result = a / b
else:
    result = "Invalid operation"

print(f"Result: {result}")

# Example 2: Age group classifier
user_age = 25
if user_age < 13:
    group = "Child"
elif user_age < 20:
    group = "Teenager"
elif user_age < 65:
    group = "Adult"
else:
    group = "Senior"

print(f"Age group: {group}")

# ---------------------------------------------
# SUMMARY:
# - Use if, elif, else for decision making
# - Conditions use comparison and logical operators
# - Code blocks are defined by indentation
# - Nested ifs allow complex conditions
# - Ternary operator for concise if-else
# - Check membership with 'in' and 'not in'