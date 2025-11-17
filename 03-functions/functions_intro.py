# ---------------------------------------------------
# Python Functions Introduction
# ---------------------------------------------------
# Functions are reusable blocks of code that perform 
# a specific task. They help in organizing code,
# reducing repetition, and making programs more modular.
# ---------------------------------------------------

# ---------------------------------------------
# BASIC FUNCTION DEFINITION
# ---------------------------------------------
# Defining a simple function
def greet():
    """A simple function that prints a greeting"""
    print("Hello, welcome to Python functions!")

# Calling the function
greet()
print("---")

# ---------------------------------------------
# FUNCTION WITH PARAMETERS
# ---------------------------------------------
def greet_person(name):
    """Function that greets a specific person"""
    print(f"Hello, {name}! Nice to meet you.")

# Calling with argument
greet_person("Hadi")
greet_person("Alice")
print("---")

# ---------------------------------------------
# FUNCTION WITH MULTIPLE PARAMETERS
# ---------------------------------------------
def introduce(name, age, city):
    """Function that introduces a person with multiple details"""
    print(f"Hi, I'm {name}, {age} years old, from {city}.")

introduce("Hadi", 26, "Mashhad")
introduce("Sarah", 30, "Tehran")
print("---")

# ---------------------------------------------
# FUNCTION WITH RETURN VALUE
# ---------------------------------------------
def add_numbers(a, b):
    """Function that returns the sum of two numbers"""
    result = a + b
    return result

# Using the return value
sum_result = add_numbers(5, 3)
print(f"5 + 3 = {sum_result}")

# Using return value directly in expression
print(f"10 + 15 = {add_numbers(10, 15)}")
print("---")

# ---------------------------------------------
# MULTIPLE RETURN VALUES
# ---------------------------------------------
def calculate_rectangle(length, width):
    """Function that returns both area and perimeter"""
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter  # Returns a tuple

# Unpacking multiple return values
rect_area, rect_perimeter = calculate_rectangle(5, 3)
print(f"Rectangle: Area = {rect_area}, Perimeter = {rect_perimeter}")

# Or receive as a tuple
result = calculate_rectangle(4, 6)
print(f"Result as tuple: {result}")
print("---")

# ---------------------------------------------
# DEFAULT PARAMETERS
# ---------------------------------------------
def greet_with_time(name, time_of_day="day"):
    """Function with default parameter"""
    print(f"Good {time_of_day}, {name}!")

# Using default value
greet_with_time("Hadi")

# Overriding default value
greet_with_time("Alice", "morning")
greet_with_time("Bob", "evening")
print("---")

# ---------------------------------------------
# KEYWORD ARGUMENTS
# ---------------------------------------------
def create_person_info(name, age, city, occupation):
    """Function demonstrating keyword arguments"""
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Occupation: {occupation}")

# Using positional arguments
create_person_info("Hadi", 26, "Mashhad", "Developer")

print()  # Empty line

# Using keyword arguments (order doesn't matter)
create_person_info(
    age=30,
    occupation="Teacher",
    name="Alice",
    city="Tehran"
)

print("---")

# ---------------------------------------------
# DOCSTRINGS AND FUNCTION DOCUMENTATION
# ---------------------------------------------
def power(base, exponent):
    """
    Calculate the power of a number.
    
    Args:
        base (float): The base number
        exponent (float): The exponent
    
    Returns:
        float: The result of base raised to exponent
    """
    return base ** exponent

# Accessing docstring
print(power.__doc__)
print(f"2^3 = {power(2, 3)}")
print("---")

# ---------------------------------------------
# SCOPE OF VARIABLES
# ---------------------------------------------
# Global variable
global_var = "I'm global"

def scope_demo():
    """Demonstrating local and global scope"""
    local_var = "I'm local"
    print(f"Inside function: {local_var}")
    print(f"Inside function: {global_var}")

scope_demo()
print(f"Outside function: {global_var}")
# print(local_var)  # This would cause an error - local_var not defined outside

print("---")

# ---------------------------------------------
# MODIFYING GLOBAL VARIABLES
# ---------------------------------------------
counter = 0

def increment_counter():
    """Modifying global variable using global keyword"""
    global counter
    counter += 1
    print(f"Counter inside function: {counter}")

print(f"Initial counter: {counter}")
increment_counter()
increment_counter()
print(f"Final counter: {counter}")
print("---")

# ---------------------------------------------
# FUNCTIONS AS FIRST-CLASS OBJECTS
# ---------------------------------------------
def square(x):
    """Return square of a number"""
    return x * x

def cube(x):
    """Return cube of a number"""
    return x * x * x

# Storing functions in variables
operation = square
print(f"Square of 4: {operation(4)}")

operation = cube
print(f"Cube of 3: {operation(3)}")

# Passing functions as arguments
def apply_operation(func, number):
    """Apply a function to a number"""
    return func(number)

print(f"apply_operation(square, 5): {apply_operation(square, 5)}")
print(f"apply_operation(cube, 2): {apply_operation(cube, 2)}")
print("---")

# ---------------------------------------------
# PRACTICAL EXAMPLES
# ---------------------------------------------

# Example 1: Temperature converter
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

print(f"20°C = {celsius_to_fahrenheit(20):.1f}°F")
print(f"68°F = {fahrenheit_to_celsius(68):.1f}°C")
print("---")

# Example 2: Grade calculator
def calculate_grade(score):
    """Calculate grade based on score"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

scores = [85, 92, 78, 45, 65]
for score in scores:
    grade = calculate_grade(score)
    print(f"Score: {score} -> Grade: {grade}")

print("---")

# Example 3: Simple calculator
def calculator(operation, a, b):
    """Simple calculator function"""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

print(f"5 + 3 = {calculator('add', 5, 3)}")
print(f"10 - 4 = {calculator('subtract', 10, 4)}")
print(f"6 * 7 = {calculator('multiply', 6, 7)}")
print(f"15 / 3 = {calculator('divide', 15, 3)}")
print("---")

# Example 4: Palindrome checker
def is_palindrome(text):
    """Check if a string is palindrome"""
    clean_text = text.lower().replace(" ", "")
    return clean_text == clean_text[::-1]

test_words = ["radar", "Python", "A man a plan a canal Panama", "hello"]
for word in test_words:
    result = is_palindrome(word)
    print(f"'{word}' is palindrome: {result}")

print("---")

# Example 5: Fibonacci sequence generator
def fibonacci(n):
    """Generate first n numbers in Fibonacci sequence"""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(f"First 10 Fibonacci numbers: {fibonacci(10)}")
print("---")

# ---------------------------------------------
# TYPE HINTS (Python 3.5+)
# ---------------------------------------------
def multiply(x: float, y: float) -> float:
    """Function with type hints"""
    return x * y

result = multiply(4.5, 2.0)
print(f"Type hinted function: 4.5 * 2.0 = {result}")

# ---------------------------------------------
# SUMMARY:
# - Use def to define functions
# - Parameters are inputs, arguments are actual values
# - Use return to send back results
# - Functions can return multiple values (as tuple)
# - Default parameters provide fallback values
# - Keyword arguments make code more readable
# - Docstrings document function purpose and usage
# - Variables have local and global scope
# - Functions are first-class objects in Python
# - Use meaningful names and proper documentation