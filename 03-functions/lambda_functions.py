# ---------------------------------------------------
# Python Lambda Functions
# ---------------------------------------------------
# Lambda functions are small, anonymous functions
# defined with the lambda keyword.
# 
# Syntax: lambda arguments: expression
# 
# They can have any number of arguments but only one expression.
# The expression is evaluated and returned.
# ---------------------------------------------------

# ---------------------------------------------
# BASIC LAMBDA FUNCTIONS
# ---------------------------------------------
# Simple lambda function
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")
print(f"Square of 8: {square(8)}")

# Lambda with multiple arguments
add = lambda a, b: a + b
print(f"3 + 4 = {add(3, 4)}")

# Lambda with no arguments
get_pi = lambda: 3.14159
print(f"PI value: {get_pi()}")

print("---")

# ---------------------------------------------
# LAMBDA VS REGULAR FUNCTION
# ---------------------------------------------
# Regular function
def multiply_regular(x, y):
    return x * y

# Lambda equivalent
multiply_lambda = lambda x, y: x * y

print(f"Regular function: 4 * 5 = {multiply_regular(4, 5)}")
print(f"Lambda function: 4 * 5 = {multiply_lambda(4, 5)}")
print("---")

# ---------------------------------------------
# USING LAMBDA WITH BUILT-IN FUNCTIONS
# ---------------------------------------------

# With map() - Apply function to all items
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared}")

# With filter() - Filter items based on condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# With sorted() - Custom sorting
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
sorted_by_length = sorted(names, key=lambda name: len(name))
print(f"Names sorted by length: {sorted_by_length}")

print("---")

# ---------------------------------------------
# LAMBDA WITH MULTIPLE PARAMETERS
# ---------------------------------------------
# Calculate area of rectangle
area = lambda length, width: length * width
print(f"Area of 5x3 rectangle: {area(5, 3)}")

# Calculate power with base and exponent
power = lambda base, exp: base ** exp
print(f"2^8 = {power(2, 8)}")

# String formatting
greet = lambda name, age: f"Hello {name}, you are {age} years old"
print(greet("Hadi", 26))

print("---")

# ---------------------------------------------
# LAMBDA WITH CONDITIONAL EXPRESSIONS
# ---------------------------------------------
# Check if number is even or odd
check_even = lambda x: "even" if x % 2 == 0 else "odd"
print(f"4 is {check_even(4)}")
print(f"7 is {check_even(7)}")

# Find maximum of two numbers
max_num = lambda a, b: a if a > b else b
print(f"Max of 10 and 15: {max_num(10, 15)}")

# Grade classifier
classify_grade = lambda score: "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(f"Score 85: {classify_grade(85)}")
print(f"Score 92: {classify_grade(92)}")
print(f"Score 65: {classify_grade(65)}")

print("---")

# ---------------------------------------------
# LAMBDA IN DATA PROCESSING
# ---------------------------------------------
# List of dictionaries
students = [
    {"name": "Alice", "age": 20, "grade": 85},
    {"name": "Bob", "age": 22, "grade": 92},
    {"name": "Charlie", "age": 19, "grade": 78},
    {"name": "Diana", "age": 21, "grade": 95}
]

# Sort by grade
sorted_by_grade = sorted(students, key=lambda student: student["grade"], reverse=True)
print("Students sorted by grade:")
for student in sorted_by_grade:
    print(f"  {student['name']}: {student['grade']}")

# Extract names only
names_only = list(map(lambda student: student["name"], students))
print(f"Student names: {names_only}")

# Filter students with grade > 80
top_students = list(filter(lambda student: student["grade"] > 80, students))
print("Top students (grade > 80):")
for student in top_students:
    print(f"  {student['name']}: {student['grade']}")

print("---")

# ---------------------------------------------
# LAMBDA WITH REDUCE()
# ---------------------------------------------
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Calculate product
product = reduce(lambda x, y: x * y, numbers)
print(f"Product of {numbers}: {product}")

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum of {numbers}: {maximum}")

# Concatenate strings
words = ["Hello", " ", "World", "!"]
sentence = reduce(lambda x, y: x + y, words)
print(f"Concatenated: {sentence}")

print("---")

# ---------------------------------------------
# LAMBDA IN LIST COMPREHENSIONS
# ---------------------------------------------
# Using lambda in list comprehensions
operations = [
    lambda x: x * 2,
    lambda x: x + 10,
    lambda x: x ** 2,
    lambda x: x - 5
]

number = 5
results = [func(number) for func in operations]
print(f"Operations on {number}: {results}")

# Create a list of lambda functions
multipliers = [lambda x, i=i: x * i for i in range(1, 6)]
for i, multiplier in enumerate(multipliers, 1):
    print(f"Multiplier {i}: 3 * {i} = {multiplier(3)}")

print("---")

# ---------------------------------------------
# LAMBDA WITH DEFAULT ARGUMENTS
# ---------------------------------------------
# Lambda with default parameter
greet_with_default = lambda name, greeting="Hello": f"{greeting}, {name}!"
print(greet_with_default("Hadi"))
print(greet_with_default("Alice", "Hi"))

# Lambda with multiple defaults
calculate = lambda a, b=1, c=1: a * b + c
print(f"calculate(5): {calculate(5)}")
print(f"calculate(5, 2): {calculate(5, 2)}")
print(f"calculate(5, 2, 10): {calculate(5, 2, 10)}")

print("---")

# ---------------------------------------------
# PRACTICAL EXAMPLES
# ---------------------------------------------

# Example 1: Simple Calculator
calculator = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y if y != 0 else "Error: Division by zero",
    "power": lambda x, y: x ** y
}

print("Calculator Operations:")
print(f"10 + 5 = {calculator['add'](10, 5)}")
print(f"10 - 5 = {calculator['subtract'](10, 5)}")
print(f"10 * 5 = {calculator['multiply'](10, 5)}")
print(f"10 / 5 = {calculator['divide'](10, 5)}")
print(f"2 ^ 3 = {calculator['power'](2, 3)}")

print("---")

# Example 2: Text Processing
texts = ["hello world", "PYTHON PROGRAMMING", "Lambda Functions", "data science"]

# Convert to title case
title_case = list(map(lambda text: text.title(), texts))
print(f"Title case: {title_case}")

# Filter short texts (length < 15)
short_texts = list(filter(lambda text: len(text) < 15, texts))
print(f"Short texts: {short_texts}")

# Count words in each text
word_counts = list(map(lambda text: len(text.split()), texts))
print(f"Word counts: {word_counts}")

print("---")

# Example 3: Mathematical Operations
import math

# Create math operations using lambda
math_operations = {
    "sqrt": lambda x: math.sqrt(x),
    "log": lambda x: math.log(x),
    "sin": lambda x: math.sin(x),
    "cos": lambda x: math.cos(x),
    "factorial": lambda x: math.factorial(int(x)) if x >= 0 else "Invalid"
}

print("Math Operations:")
print(f"sqrt(16) = {math_operations['sqrt'](16)}")
print(f"log(100) = {math_operations['log'](100):.2f}")
print(f"sin(π/2) = {math_operations['sin'](math.pi/2):.2f}")
print(f"cos(π) = {math_operations['cos'](math.pi):.2f}")
print(f"factorial(5) = {math_operations['factorial'](5)}")

print("---")

# Example 4: Data Validation
# Lambda functions for validation rules
validation_rules = {
    "is_positive": lambda x: x > 0,
    "is_even": lambda x: x % 2 == 0,
    "is_valid_email": lambda email: "@" in email and "." in email,
    "is_strong_password": lambda pwd: len(pwd) >= 8 and any(c.isupper() for c in pwd) and any(c.isdigit() for c in pwd)
}

test_data = [
    ("number", 10, "is_positive"),
    ("number", -5, "is_positive"),
    ("email", "user@example.com", "is_valid_email"),
    ("email", "invalid-email", "is_valid_email"),
    ("password", "StrongPass123", "is_strong_password"),
    ("password", "weak", "is_strong_password")
]

print("Data Validation:")
for data_type, value, rule in test_data:
    result = validation_rules[rule](value)
    status = "PASS" if result else "FAIL"
    print(f"  {data_type} '{value}' - {rule}: {status}")

print("---")

# Example 5: Custom Sorting with Multiple Criteria
products = [
    {"name": "Laptop", "price": 1000, "rating": 4.5},
    {"name": "Mouse", "price": 25, "rating": 4.2},
    {"name": "Keyboard", "price": 75, "rating": 4.7},
    {"name": "Monitor", "price": 300, "rating": 4.3},
    {"name": "Headphones", "price": 150, "rating": 4.6}
]

# Sort by price (ascending)
sorted_by_price = sorted(products, key=lambda p: p["price"])
print("Products sorted by price:")
for product in sorted_by_price:
    print(f"  {product['name']}: ${product['price']}")

# Sort by rating (descending) then by price (ascending)
sorted_by_rating_price = sorted(products, key=lambda p: (-p["rating"], p["price"]))
print("\nProducts sorted by rating (desc) then price (asc):")
for product in sorted_by_rating_price:
    print(f"  {product['name']}: ${product['price']}, Rating: {product['rating']}")

print("---")

# ---------------------------------------------
# LAMBDA IN FUNCTIONAL PROGRAMMING
# ---------------------------------------------
# Higher-order functions with lambda

def create_multiplier(factor):
    """Returns a function that multiplies by the given factor"""
    return lambda x: x * factor

double = create_multiplier(2)
triple = create_multiplier(3)

print(f"Double 5: {double(5)}")
print(f"Triple 5: {triple(5)}")

# Function composition
def compose(f, g):
    """Compose two functions: f(g(x))"""
    return lambda x: f(g(x))

add_one = lambda x: x + 1
square = lambda x: x ** 2

add_then_square = compose(square, add_one)
square_then_add = compose(add_one, square)

print(f"Add then square (2): {add_then_square(2)}")  # (2+1)^2 = 9
print(f"Square then add (2): {square_then_add(2)}")  # (2^2)+1 = 5

print("---")

# ---------------------------------------------
# LIMITATIONS OF LAMBDA FUNCTIONS
# ---------------------------------------------
# Lambda functions have limitations:

# 1. Only one expression
# This is valid:
simple = lambda x: x * 2

# This would be invalid (multiple statements):
# complex_lambda = lambda x: 
#     result = x * 2
#     print(result)
#     return result

# 2. No statements, only expressions
# valid_lambda = lambda x: x + 1
# invalid_lambda = lambda x: print(x)  # print is a statement

# 3. For complex logic, use regular functions
def complex_operation(x):
    """Regular function for complex operations"""
    if x < 0:
        return "Negative"
    elif x == 0:
        return "Zero"
    else:
        return "Positive"

# Equivalent with lambda (less readable):
complex_lambda = lambda x: "Negative" if x < 0 else "Zero" if x == 0 else "Positive"

print(f"Regular function: {complex_operation(5)}")
print(f"Lambda function: {complex_lambda(5)}")

print("---")

# ---------------------------------------------
# WHEN TO USE LAMBDA FUNCTIONS
# ---------------------------------------------
"""
Use lambda functions for:
- Simple, one-line operations
- Functions that are used only once
- As arguments to higher-order functions (map, filter, sorted)
- When you need a quick, throwaway function

Avoid lambda functions for:
- Complex logic with multiple steps
- Functions that need documentation
- Functions that will be reused multiple times
- When readability is important
"""

# ---------------------------------------------
# SUMMARY:
# - Lambda functions are anonymous, one-line functions
# - Syntax: lambda arguments: expression
# - Useful with map(), filter(), sorted(), reduce()
# - Can have multiple arguments but only one expression
# - Good for simple operations and functional programming
# - Limited compared to regular functions
# - Use judiciously for better code readability