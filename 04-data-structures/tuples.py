# ---------------------------------------------------
# Python Tuples
# ---------------------------------------------------
# Tuples are ordered, immutable collections of items.
# They are similar to lists but cannot be modified after creation.
# Tuples are defined using parentheses () or just commas.
# ---------------------------------------------------

# ---------------------------------------------
# TUPLE CREATION
# ---------------------------------------------
# Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

# Tuple with one element (note the comma)
single_element = (42,)  # Comma is required for single element
print(f"Single element tuple: {single_element}")

# Without comma - this is not a tuple!
not_a_tuple = (42)
print(f"Without comma (not tuple): {not_a_tuple} - type: {type(not_a_tuple)}")

# Multiple elements
fruits = ("apple", "banana", "cherry")
print(f"Fruits tuple: {fruits}")

# Without parentheses (tuple packing)
colors = "red", "green", "blue"
print(f"Colors without parentheses: {colors}")

# Using tuple() constructor
from_list = tuple([1, 2, 3, 4])
print(f"From list: {from_list}")

from_string = tuple("hello")
print(f"From string: {from_string}")

print("---")

# ---------------------------------------------
# TUPLE INDEXING AND SLICING
# ---------------------------------------------
numbers = (10, 20, 30, 40, 50, 60)

# Positive indexing
print(f"numbers[0]: {numbers[0]}")    # First element
print(f"numbers[2]: {numbers[2]}")    # Third element

# Negative indexing
print(f"numbers[-1]: {numbers[-1]}")  # Last element
print(f"numbers[-2]: {numbers[-2]}")  # Second last

# Slicing (same as lists)
print(f"numbers[1:4]: {numbers[1:4]}")    # Elements 1 to 3
print(f"numbers[:3]: {numbers[:3]}")      # First 3 elements
print(f"numbers[2:]: {numbers[2:]}")      # From index 2 to end
print(f"numbers[::2]: {numbers[::2]}")    # Every second element
print(f"numbers[::-1]: {numbers[::-1]}")  # Reversed tuple

print("---")

# ---------------------------------------------
# TUPLE IMMUTABILITY
# ---------------------------------------------
# Tuples are immutable - cannot be changed after creation
immutable_tuple = (1, 2, 3)

# This would cause an error:
# immutable_tuple[0] = 100  # TypeError: 'tuple' object does not support item assignment

# But we can create new tuples from existing ones
new_tuple = immutable_tuple + (4, 5)
print(f"Original: {immutable_tuple}")
print(f"New tuple: {new_tuple}")

# However, if a tuple contains mutable objects, those can be modified
mixed_tuple = (1, 2, [3, 4])
print(f"Before modification: {mixed_tuple}")
mixed_tuple[2][0] = 100  # Modifying the list inside tuple
print(f"After modification: {mixed_tuple}")

print("---")

# ---------------------------------------------
# TUPLE OPERATIONS
# ---------------------------------------------
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
combined = tuple1 + tuple2
print(f"tuple1 + tuple2: {combined}")

# Repetition
repeated = tuple1 * 3
print(f"tuple1 * 3: {repeated}")

# Membership testing
print(f"2 in tuple1: {2 in tuple1}")
print(f"7 in tuple1: {7 in tuple1}")

# Length
print(f"Length of tuple1: {len(tuple1)}")

# Comparison
tuple_a = (1, 2, 3)
tuple_b = (1, 2, 3)
tuple_c = (1, 2, 4)
print(f"tuple_a == tuple_b: {tuple_a == tuple_b}")
print(f"tuple_a == tuple_c: {tuple_a == tuple_c}")
print(f"tuple_a < tuple_c: {tuple_a < tuple_c}")  # Lexicographical comparison

print("---")

# ---------------------------------------------
# TUPLE METHODS
# ---------------------------------------------
# Tuples have only two methods: count() and index()

numbers = (1, 2, 3, 2, 4, 2, 5, 2)

# count() - count occurrences of an element
count_2 = numbers.count(2)
print(f"Count of 2: {count_2}")

# index() - find first occurrence of an element
first_2 = numbers.index(2)
print(f"First occurrence of 2: {first_2}")

# index() with start and end
second_2 = numbers.index(2, 2)  # Start searching from index 2
print(f"Second occurrence of 2: {second_2}")

print("---")

# ---------------------------------------------
# TUPLE UNPACKING
# ---------------------------------------------
# Basic unpacking
person = ("John", 30, "Engineer")
name, age, profession = person
print(f"Name: {name}, Age: {age}, Profession: {profession}")

# Unpacking with asterisk (*) for multiple elements
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Ignoring elements with underscore
coordinates = (10, 20, 30)
x, y, _ = coordinates
print(f"X: {x}, Y: {y}")

# Swapping variables using tuples
a, b = 5, 10
print(f"Before swap: a={a}, b={b}")
a, b = b, a  # This is tuple packing and unpacking
print(f"After swap: a={a}, b={b}")

print("---")

# ---------------------------------------------
# TUPLE VS LIST
# ---------------------------------------------
import sys
import timeit

# Memory comparison
list_obj = [1, 2, 3, 4, 5]
tuple_obj = (1, 2, 3, 4, 5)

print(f"List size: {sys.getsizeof(list_obj)} bytes")
print(f"Tuple size: {sys.getsizeof(tuple_obj)} bytes")

# Performance comparison
list_time = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_time = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)

print(f"List creation time: {list_time:.6f} seconds")
print(f"Tuple creation time: {tuple_time:.6f} seconds")

print("---")

# ---------------------------------------------
# NESTED TUPLES
# ---------------------------------------------
# Tuples can contain other tuples
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print("Matrix:")
for row in matrix:
    print(f"  {row}")

# Accessing nested elements
print(f"matrix[1][2]: {matrix[1][2]}")  # Second row, third column

# Complex nested structure
employee = (
    "Alice",
    28,
    ("Software Engineer", 75000),
    ["Python", "Java", "SQL"]
)

print(f"Employee: {employee}")
print(f"Job title: {employee[2][0]}")
print(f"Salary: ${employee[2][1]}")

print("---")

# ---------------------------------------------
# TUPLES AS DICTIONARY KEYS
# ---------------------------------------------
# Tuples can be used as dictionary keys (unlike lists)
locations = {
    (35.6895, 139.6917): "Tokyo",
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278): "London"
}

print("Location coordinates:")
for coords, city in locations.items():
    print(f"  {coords} -> {city}")

# This would work:
locations[(48.8566, 2.3522)] = "Paris"
print(f"After adding Paris: {locations}")

print("---")

# ---------------------------------------------
# PRACTICAL EXAMPLES
# ---------------------------------------------

# Example 1: RGB Colors
colors = [
    ("red", (255, 0, 0)),
    ("green", (0, 255, 0)),
    ("blue", (0, 0, 255)),
    ("yellow", (255, 255, 0))
]

print("Color values:")
for name, rgb in colors:
    print(f"  {name}: {rgb}")

print("---")

# Example 2: Student Records
students = [
    ("Alice", 85, "A"),
    ("Bob", 92, "A"),
    ("Charlie", 78, "C"),
    ("Diana", 65, "D")
]

print("Student records:")
for name, score, grade in students:
    print(f"  {name}: Score={score}, Grade={grade}")

# Sort by score
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print("\nStudents sorted by score:")
for name, score, grade in sorted_students:
    print(f"  {name}: {score}")

print("---")

# Example 3: Function returning multiple values
def get_circle_properties(radius):
    """Calculate circle properties"""
    import math
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference  # Returns a tuple

circle_info = get_circle_properties(5)
area, circumference = circle_info
print(f"Circle with radius 5:")
print(f"  Area: {area:.2f}")
print(f"  Circumference: {circumference:.2f}")

# Direct unpacking
a, c = get_circle_properties(3)
print(f"Circle with radius 3 - Area: {a:.2f}, Circumference: {c:.2f}")

print("---")

# Example 4: Database-like records
products = [
    (1, "Laptop", 999.99, "Electronics"),
    (2, "Book", 19.99, "Education"),
    (3, "Shirt", 29.99, "Clothing"),
    (4, "Phone", 499.99, "Electronics")
]

print("Product Catalog:")
for id, name, price, category in products:
    print(f"  {id}: {name} - ${price} ({category})")

# Filter electronics
electronics = [product for product in products if product[3] == "Electronics"]
print("\nElectronics products:")
for product in electronics:
    print(f"  {product[1]} - ${product[2]}")

print("---")

# Example 5: Coordinate system
points = [
    (0, 0),
    (1, 2),
    (3, 1),
    (2, 4),
    (5, 3)
]

def distance(p1, p2):
    """Calculate Euclidean distance between two points"""
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

print("Distance from origin (0,0):")
for point in points:
    dist = distance((0, 0), point)
    print(f"  {point}: {dist:.2f}")

print("---")

# Example 6: Date representations
dates = [
    (2024, 1, 15),
    (2024, 3, 22),
    (2024, 6, 10),
    (2024, 12, 25)
]

print("Important dates (YYYY-MM-DD):")
for year, month, day in dates:
    print(f"  {year}-{month:02d}-{day:02d}")

# Sort by month and day
sorted_dates = sorted(dates, key=lambda x: (x[1], x[2]))
print("\nDates sorted by month and day:")
for date in sorted_dates:
    print(f"  {date[0]}-{date[1]:02d}-{date[2]:02d}")

print("---")

# ---------------------------------------------
# NAMEDTUPLES (Collections Module)
# ---------------------------------------------
from collections import namedtuple

# Creating a namedtuple type
Person = namedtuple('Person', ['name', 'age', 'city'])

# Creating instances
person1 = Person("Hadi", 26, "Mashhad")
person2 = Person("Alice", 30, "Tehran")

print("Namedtuple examples:")
print(f"person1: {person1}")
print(f"person1.name: {person1.name}")
print(f"person1.age: {person1.age}")
print(f"person1.city: {person1.city}")

# Namedtuples are still tuples
print(f"Index access: {person1[0]}")  # Still works
print(f"Length: {len(person1)}")

# Convert to dictionary
print(f"As dict: {person1._asdict()}")

print("---")

# ---------------------------------------------
# ZIP FUNCTION WITH TUPLES
# ---------------------------------------------
names = ("Alice", "Bob", "Charlie")
ages = (25, 30, 35)
cities = ("New York", "London", "Paris")

# Zip returns tuples
zipped = list(zip(names, ages, cities))
print("Zipped data:")
for item in zipped:
    print(f"  {item}")

# Unzipping
unzipped_names, unzipped_ages, unzipped_cities = zip(*zipped)
print(f"Unzipped names: {unzipped_names}")
print(f"Unzipped ages: {unzipped_ages}")
print(f"Unzipped cities: {unzipped_cities}")

print("---")

# ---------------------------------------------
# WHEN TO USE TUPLES VS LISTS
# ---------------------------------------------
"""
Use TUPLES when:
- Data shouldn't change (immutable)
- Using as dictionary keys
- Function returning multiple values
- Heterogeneous data (different types)
- Performance is critical

Use LISTS when:
- Data needs to be modified
- Homogeneous data (same type)
- Need methods like append(), remove(), sort()
- Building collections dynamically
"""

# Example demonstrating the difference
# Fixed configuration - use tuple
DATABASE_CONFIG = ("localhost", 5432, "my_database", "readonly")

# Dynamic collection - use list
user_sessions = []
user_sessions.append("session_1")
user_sessions.append("session_2")

print(f"Database config (tuple): {DATABASE_CONFIG}")
print(f"User sessions (list): {user_sessions}")

print("---")

# ---------------------------------------------
# TUPLE COMPREHENSIONS?
# ---------------------------------------------
# There are no tuple comprehensions, but we can use generator expressions
numbers = [1, 2, 3, 4, 5]

# This creates a generator, then converts to tuple
squared_tuple = tuple(x**2 for x in numbers)
print(f"Squared tuple: {squared_tuple}")

# With condition
even_squares = tuple(x**2 for x in numbers if x % 2 == 0)
print(f"Even squares tuple: {even_squares}")

print("---")

# ---------------------------------------------
# SUMMARY:
# - Tuples are immutable, ordered collections
# - Use () for creation, but comma is required for single elements
# - Support indexing, slicing, and iteration like lists
# - More memory efficient and faster than lists
# - Can be used as dictionary keys
# - Support tuple unpacking for multiple assignment
# - Only two methods: count() and index()
# - Use for heterogeneous data that shouldn't change
# - namedtuple provides named fields for better readability
# - No tuple comprehensions, but use generator expressions with tuple()