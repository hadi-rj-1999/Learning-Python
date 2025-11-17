# ---------------------------------------------------
# Python Function Arguments and Parameters
# ---------------------------------------------------
# This file covers different types of function arguments
# and parameters in Python, including:
# - Positional arguments
# - Keyword arguments  
# - Default parameters
# - Variable-length arguments (*args, **kwargs)
# - Argument unpacking
# ---------------------------------------------------

# ---------------------------------------------
# POSITIONAL ARGUMENTS
# ---------------------------------------------
def student_info(name, age, grade):
    """Function with positional arguments"""
    print(f"Student: {name}")
    print(f"Age: {age}")
    print(f"Grade: {grade}")
    print("-" * 20)

# Must provide arguments in correct order
student_info("Ali", 15, "A")
student_info("Sara", 16, "B")
print("---")

# ---------------------------------------------
# KEYWORD ARGUMENTS
# ---------------------------------------------
def person_details(name, age, city, occupation):
    """Function demonstrating keyword arguments"""
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Occupation: {occupation}")
    print("-" * 20)

# Using keyword arguments (order doesn't matter)
person_details(name="Hadi", age=26, city="Mashhad", occupation="Developer")
person_details(occupation="Teacher", city="Tehran", age=30, name="Maryam")
print("---")

# ---------------------------------------------
# MIXING POSITIONAL AND KEYWORD ARGUMENTS
# ---------------------------------------------
def mixed_arguments(a, b, c, d):
    """Function with mixed argument types"""
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")

# Positional first, then keyword
mixed_arguments(1, 2, c=3, d=4)

# This would cause error: positional after keyword
# mixed_arguments(1, b=2, 3, d=4)  # INVALID!
print("---")

# ---------------------------------------------
# DEFAULT PARAMETERS
# ---------------------------------------------
def greet(name, message="Hello", punctuation="!"):
    """Function with default parameters"""
    print(f"{message}, {name}{punctuation}")

# Using default values
greet("Hadi")

# Overriding some defaults
greet("Alice", "Hi")
greet("Bob", "Welcome", "!!!")

# Using keyword to override specific defaults
greet("Charlie", punctuation="?")
print("---")

# ---------------------------------------------
# VARIABLE-LENGTH ARGUMENTS (*args)
# ---------------------------------------------
def sum_numbers(*args):
    """Function that accepts any number of positional arguments"""
    print(f"Arguments received: {args}")
    print(f"Type of args: {type(args)}")  # It's a tuple
    total = sum(args)
    print(f"Sum: {total}")
    return total

# Calling with different number of arguments
sum_numbers(1, 2)
sum_numbers(1, 2, 3, 4, 5)
sum_numbers(10, 20, 30)
print("---")

def average(*numbers):
    """Calculate average of any number of values"""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

print(f"Average of 1, 2, 3: {average(1, 2, 3)}")
print(f"Average of 10, 20, 30, 40: {average(10, 20, 30, 40)}")
print("---")

# ---------------------------------------------
# KEYWORD VARIABLE-LENGTH ARGUMENTS (**kwargs)
# ---------------------------------------------
def print_student_info(**kwargs):
    """Function that accepts any number of keyword arguments"""
    print(f"Keyword arguments received: {kwargs}")
    print(f"Type of kwargs: {type(kwargs)}")  # It's a dictionary
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
    print("-" * 20)

# Calling with different keyword arguments
print_student_info(name="Ali", age=15, grade="A")
print_student_info(first_name="Sara", last_name="Smith", city="Tehran", country="Iran")
print("---")

def create_student_profile(**details):
    """Create a student profile from keyword arguments"""
    profile = {
        "name": details.get("name", "Unknown"),
        "age": details.get("age", 0),
        "grade": details.get("grade", "Not specified"),
        "subjects": details.get("subjects", [])
    }
    return profile

student1 = create_student_profile(name="Hadi", age=26, grade="A", subjects=["Math", "Physics"])
student2 = create_student_profile(name="Maryam", city="Tehran")  # Missing some info
print(f"Student 1: {student1}")
print(f"Student 2: {student2}")
print("---")

# ---------------------------------------------
# COMBINING *args AND **kwargs
# ---------------------------------------------
def flexible_function(*args, **kwargs):
    """Function that accepts both positional and keyword arguments"""
    print("Positional arguments (*args):")
    for i, arg in enumerate(args):
        print(f"  arg{i}: {arg}")
    
    print("Keyword arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")
    
    print("-" * 20)

# Examples
flexible_function(1, 2, 3, name="Hadi", city="Mashhad")
flexible_function("apple", "banana", color="red", size="large", price=100)
print("---")

# ---------------------------------------------
# ARGUMENT UNPACKING (* and ** operators)
# ---------------------------------------------
def describe_pet(animal_type, pet_name, age=None):
    """Function to describe a pet"""
    description = f"I have a {animal_type} named {pet_name}."
    if age:
        description += f" It is {age} years old."
    print(description)

# Normal call
describe_pet("dog", "Rex", 3)

# Using argument unpacking
pet_info = ["cat", "Whiskers", 2]
describe_pet(*pet_info)  # Unpacks list into positional arguments

pet_dict = {"animal_type": "bird", "pet_name": "Tweety", "age": 1}
describe_pet(**pet_dict)  # Unpacks dictionary into keyword arguments
print("---")

# ---------------------------------------------
# FUNCTION WITH ALL ARGUMENT TYPES
# ---------------------------------------------
def comprehensive_function(a, b, c=10, *args, d=20, e=30, **kwargs):
    """
    Function demonstrating all types of parameters:
    - a, b: required positional
    - c: default parameter
    - *args: variable positional
    - d, e: keyword-only with defaults
    - **kwargs: variable keyword
    """
    print(f"a: {a}, b: {b}, c: {c}")
    print(f"args: {args}")
    print(f"d: {d}, e: {e}")
    print(f"kwargs: {kwargs}")
    print("-" * 20)

# Examples
comprehensive_function(1, 2)
comprehensive_function(1, 2, 3, 4, 5, d=40, name="Hadi")
comprehensive_function(1, 2, 3, 4, 5, 6, d=40, e=50, city="Mashhad", country="Iran")
print("---")

# ---------------------------------------------
# KEYWORD-ONLY ARGUMENTS
# ---------------------------------------------
def send_email(to, *, subject, body, cc=None):
    """
    Function with keyword-only arguments after *
    Arguments after * must be passed as keyword arguments
    """
    print(f"To: {to}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    if cc:
        print(f"CC: {cc}")
    print("-" * 20)

# Valid calls
send_email("hadi@example.com", subject="Hello", body="This is a test email")
send_email("friend@example.com", subject="Meeting", body="Let's meet tomorrow", cc="boss@example.com")

# This would cause error: subject and body must be keyword arguments
# send_email("test@example.com", "Hello", "This is a test")  # INVALID!
print("---")

# ---------------------------------------------
# POSITIONAL-ONLY ARGUMENTS (Python 3.8+)
# ---------------------------------------------
def old_style_function(x, y, /, z):
    """
    Function with positional-only arguments before /
    Arguments before / must be passed as positional arguments
    """
    print(f"x: {x}, y: {y}, z: {z}")

# Valid calls
old_style_function(1, 2, 3)
old_style_function(1, 2, z=3)

# This would cause error: x and y must be positional arguments
# old_style_function(x=1, y=2, z=3)  # INVALID!
print("---")

# ---------------------------------------------
# PRACTICAL EXAMPLES
# ---------------------------------------------

# Example 1: Configurable logger
def logger(message, level="INFO", *, timestamp=True, color=None):
    """Configurable logging function with keyword-only options"""
    import datetime
    
    if timestamp:
        timestamp_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"[{timestamp_str}] {message}"
    
    prefix = f"{level}: "
    
    # Simple color simulation (in real use, you might use colorama library)
    color_codes = {
        "red": "\033[91m",
        "green": "\033[92m", 
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "reset": "\033[0m"
    }
    
    if color in color_codes:
        message = f"{color_codes[color]}{prefix}{message}{color_codes['reset']}"
    else:
        message = f"{prefix}{message}"
    
    print(message)

logger("Application started")
logger("Warning: Disk space low", "WARNING", color="yellow")
logger("Error: Connection failed", "ERROR", timestamp=False, color="red")
print("---")

# Example 2: Flexible shopping cart
def calculate_total(*prices, discount=0, tax_rate=0):
    """Calculate total with flexible items and optional discount/tax"""
    subtotal = sum(prices)
    
    if discount > 0:
        subtotal -= subtotal * (discount / 100)
    
    if tax_rate > 0:
        subtotal += subtotal * (tax_rate / 100)
    
    return subtotal

print(f"Total: ${calculate_total(10, 20, 30):.2f}")
print(f"Total with 10% discount: ${calculate_total(10, 20, 30, discount=10):.2f}")
print(f"Total with tax: ${calculate_total(15, 25, 35, tax_rate=8):.2f}")
print(f"Total with discount and tax: ${calculate_total(15, 25, 35, discount=15, tax_rate=8):.2f}")
print("---")

# Example 3: Database query builder
def build_query(table, *columns, where=None, order_by=None, limit=None, **filters):
    """Build SQL-like query with flexible parameters"""
    query_parts = []
    
    # SELECT columns
    if columns:
        columns_str = ", ".join(columns)
    else:
        columns_str = "*"
    
    query_parts.append(f"SELECT {columns_str} FROM {table}")
    
    # WHERE conditions
    conditions = []
    if where:
        conditions.append(where)
    
    for field, value in filters.items():
        conditions.append(f"{field} = '{value}'")
    
    if conditions:
        query_parts.append(f"WHERE {' AND '.join(conditions)}")
    
    # ORDER BY
    if order_by:
        query_parts.append(f"ORDER BY {order_by}")
    
    # LIMIT
    if limit:
        query_parts.append(f"LIMIT {limit}")
    
    return " ".join(query_parts)

# Example queries
query1 = build_query("users", "name", "email", city="Mashhad", age=25)
query2 = build_query("products", "name", "price", where="price > 100", order_by="price DESC", limit=10)
query3 = build_query("orders", limit=5)

print("Query 1:", query1)
print("Query 2:", query2)
print("Query 3:", query3)
print("---")

# Example 4: Function wrapper with flexible arguments
def timer(func):
    """Decorator to measure function execution time"""
    import time
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    
    return wrapper

@timer
def slow_function():
    """A function that takes some time"""
    import time
    time.sleep(1)
    return "Done"

@timer
def process_data(data, multiplier=1):
    """Process data with optional multiplier"""
    return [x * multiplier for x in data]

# Test the timed functions
slow_function()
process_data([1, 2, 3, 4, 5], multiplier=2)
print("---")

# ---------------------------------------------
# ARGUMENT VALIDATION
# ---------------------------------------------
def validate_arguments(*, min_value=0, max_value=100):
    """Decorator factory for argument validation"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Validate positional arguments
            for arg in args:
                if isinstance(arg, (int, float)) and not (min_value <= arg <= max_value):
                    raise ValueError(f"Argument {arg} is outside allowed range [{min_value}, {max_value}]")
            
            # Validate keyword arguments
            for key, value in kwargs.items():
                if isinstance(value, (int, float)) and not (min_value <= value <= max_value):
                    raise ValueError(f"Argument {key}={value} is outside allowed range [{min_value}, {max_value}]")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_arguments(min_value=1, max_value=10)
def multiply_numbers(a, b):
    return a * b

print(f"Valid: 3 * 4 = {multiply_numbers(3, 4)}")

try:
    multiply_numbers(15, 2)  # Should raise error
except ValueError as e:
    print(f"Error: {e}")
print("---")

# ---------------------------------------------
# SUMMARY:
# - Positional args: passed in order
# - Keyword args: passed with parameter names
# - Default params: have default values
# - *args: collects extra positional arguments as tuple
# - **kwargs: collects extra keyword arguments as dict
# - Argument unpacking: * for sequences, ** for dictionaries
# - Keyword-only: after * in parameter list
# - Positional-only: before / in parameter list
# - Use appropriate argument types for flexible and clear APIs