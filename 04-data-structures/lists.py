# ---------------------------------------------------
# Python Lists
# ---------------------------------------------------
# Lists are ordered, mutable collections of items.
# They can contain elements of different data types.
# Lists are defined using square brackets [].
# ---------------------------------------------------

# ---------------------------------------------
# LIST CREATION
# ---------------------------------------------
# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with integers
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# List with mixed data types
mixed_list = [1, "hello", 3.14, True, [1, 2, 3]]
print(f"Mixed list: {mixed_list}")

# List with duplicate elements
duplicates = [1, 2, 2, 3, 3, 3]
print(f"Duplicates: {duplicates}")

# Using list() constructor
from_string = list("hello")
print(f"From string: {from_string}")

from_range = list(range(5))
print(f"From range: {from_range}")

print("---")

# ---------------------------------------------
# LIST INDEXING AND SLICING
# ---------------------------------------------
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Positive indexing (from start)
print(f"fruits[0]: {fruits[0]}")    # First element
print(f"fruits[2]: {fruits[2]}")    # Third element

# Negative indexing (from end)
print(f"fruits[-1]: {fruits[-1]}")  # Last element
print(f"fruits[-2]: {fruits[-2]}")  # Second last

# List slicing [start:stop:step]
print(f"fruits[1:4]: {fruits[1:4]}")      # Elements 1 to 3
print(f"fruits[:3]: {fruits[:3]}")        # First 3 elements
print(f"fruits[2:]: {fruits[2:]}")        # From index 2 to end
print(f"fruits[::2]: {fruits[::2]}")      # Every second element
print(f"fruits[::-1]: {fruits[::-1]}")    # Reversed list

print("---")

# ---------------------------------------------
# LIST METHODS - ADDING ELEMENTS
# ---------------------------------------------
colors = ["red", "green"]

# append() - add single element to end
colors.append("blue")
print(f"After append: {colors}")

# extend() - add multiple elements
colors.extend(["yellow", "purple"])
print(f"After extend: {colors}")

# insert() - insert at specific position
colors.insert(1, "orange")
print(f"After insert: {colors}")

# Using + operator
new_colors = colors + ["pink", "brown"]
print(f"After +: {new_colors}")

print("---")

# ---------------------------------------------
# LIST METHODS - REMOVING ELEMENTS
# ---------------------------------------------
numbers = [1, 2, 3, 4, 5, 3, 6, 3]

# remove() - remove first occurrence
numbers.remove(3)
print(f"After remove(3): {numbers}")

# pop() - remove and return element at index
popped = numbers.pop(2)
print(f"Popped element: {popped}")
print(f"After pop(2): {numbers}")

# pop() without index - removes last element
last = numbers.pop()
print(f"Last element: {last}")
print(f"After pop(): {numbers}")

# del statement
del numbers[0]
print(f"After del numbers[0]: {numbers}")

# Clear all elements
numbers.clear()
print(f"After clear: {numbers}")

print("---")

# ---------------------------------------------
# LIST METHODS - SEARCHING AND INFORMATION
# ---------------------------------------------
fruits = ["apple", "banana", "cherry", "date", "banana"]

# index() - find first occurrence
banana_index = fruits.index("banana")
print(f"First banana at index: {banana_index}")

# count() - count occurrences
banana_count = fruits.count("banana")
print(f"Banana count: {banana_count}")

# in operator - check membership
has_apple = "apple" in fruits
has_mango = "mango" in fruits
print(f"Has apple: {has_apple}")
print(f"Has mango: {has_mango}")

# len() - get length
print(f"Length: {len(fruits)}")

print("---")

# ---------------------------------------------
# LIST METHODS - SORTING AND REVERSING
# ---------------------------------------------
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() - in-place sorting
numbers.sort()
print(f"Sorted: {numbers}")

# sort() descending
numbers.sort(reverse=True)
print(f"Sorted descending: {numbers}")

# sorted() - returns new sorted list
unsorted = [3, 1, 4, 1, 5]
sorted_list = sorted(unsorted)
print(f"Original: {unsorted}")
print(f"Sorted copy: {sorted_list}")

# reverse() - reverse in-place
numbers.reverse()
print(f"Reversed: {numbers}")

print("---")

# ---------------------------------------------
# LIST COMPREHENSIONS
# ---------------------------------------------
# Basic list comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# With condition
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Multiple conditions
numbers = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
print(f"Numbers divisible by 2 and 3: {numbers}")

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")

print("---")

# ---------------------------------------------
# LIST COPYING
# ---------------------------------------------
original = [1, 2, 3, [4, 5]]

# Shallow copy (different methods)
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]

# Modifying copies
copy1[0] = 100
copy1[3][0] = 400

print(f"Original: {original}")
print(f"Copy1: {copy1}")
print(f"Copy2: {copy2}")

# Deep copy (for nested structures)
import copy
deep_copy = copy.deepcopy(original)
deep_copy[3][1] = 500
print(f"Deep copy: {deep_copy}")
print(f"Original after deep copy: {original}")

print("---")

# ---------------------------------------------
# NESTED LISTS (2D ARRAYS)
# ---------------------------------------------
# Creating a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

# Accessing elements
print(f"matrix[1][2]: {matrix[1][2]}")  # Second row, third column

# Modifying nested list
matrix[0][1] = 20
print("Modified matrix:")
for row in matrix:
    print(row)

print("---")

# ---------------------------------------------
# LIST OPERATIONS
# ---------------------------------------------
a = [1, 2, 3]
b = [4, 5, 6]

# Concatenation
combined = a + b
print(f"a + b: {combined}")

# Repetition
repeated = a * 3
print(f"a * 3: {repeated}")

# Comparison
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]
print(f"list1 == list2: {list1 == list2}")
print(f"list1 == list3: {list1 == list3}")

print("---")

# ---------------------------------------------
# PRACTICAL EXAMPLES
# ---------------------------------------------

# Example 1: Shopping cart
cart = []
cart.append({"item": "Apple", "price": 1.5, "quantity": 2})
cart.append({"item": "Banana", "price": 0.8, "quantity": 5})
cart.append({"item": "Milk", "price": 2.5, "quantity": 1})

print("Shopping Cart:")
for item in cart:
    print(f"  {item['quantity']} x {item['item']} - ${item['price']} each")

# Calculate total
total = sum(item["price"] * item["quantity"] for item in cart)
print(f"Total: ${total:.2f}")

print("---")

# Example 2: Student grades
students = ["Alice", "Bob", "Charlie", "Diana"]
grades = [
    [85, 90, 78],
    [92, 88, 95],
    [76, 82, 80],
    [88, 85, 90]
]

print("Student Averages:")
for i, student in enumerate(students):
    average = sum(grades[i]) / len(grades[i])
    print(f"  {student}: {average:.1f}")

print("---")

# Example 3: Finding duplicates
numbers = [1, 2, 3, 2, 4, 5, 3, 6, 1]
duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print(f"Numbers: {numbers}")
print(f"Duplicates: {duplicates}")

print("---")

# Example 4: List as stack (LIFO)
stack = []
stack.append("task1")  # push
stack.append("task2")
stack.append("task3")

print(f"Stack: {stack}")
while stack:
    task = stack.pop()  # pop
    print(f"Processing: {task}")

print("---")

# Example 5: List as queue (FIFO)
from collections import deque
queue = deque(["person1", "person2", "person3"])
queue.append("person4")  # enqueue
print(f"Queue: {list(queue)}")

served = queue.popleft()  # dequeue
print(f"Served: {served}")
print(f"Queue after serving: {list(queue)}")

print("---")

# Example 6: Filtering and transforming data
products = [
    {"name": "Laptop", "price": 1000, "category": "electronics"},
    {"name": "Shirt", "price": 25, "category": "clothing"},
    {"name": "Book", "price": 15, "category": "education"},
    {"name": "Phone", "price": 500, "category": "electronics"}
]

# Get expensive electronics
expensive_electronics = [
    product["name"] 
    for product in products 
    if product["category"] == "electronics" and product["price"] > 300
]
print(f"Expensive electronics: {expensive_electronics}")

print("---")

# ---------------------------------------------
# LIST PERFORMANCE TIPS
# ---------------------------------------------
import time

# Bad: Repeated concatenation
def slow_concat():
    result = []
    for i in range(10000):
        result = result + [i]  # This creates new list each time
    return result

# Good: Using append
def fast_concat():
    result = []
    for i in range(10000):
        result.append(i)  # This modifies list in-place
    return result

# Timing comparison (uncomment to test)
# start = time.time()
# slow_concat()
# print(f"Slow method: {time.time() - start:.4f} seconds")

# start = time.time()
# fast_concat()
# print(f"Fast method: {time.time() - start:.4f} seconds")

print("---")

# ---------------------------------------------
# COMMON LIST PATTERNS
# ---------------------------------------------

# Pattern 1: Removing items while iterating
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Safe way: create new list
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {even_numbers}")

# Pattern 2: Finding all indices of an element
def find_all_indices(lst, value):
    return [i for i, x in enumerate(lst) if x == value]

numbers = [1, 2, 3, 2, 4, 2, 5]
indices = find_all_indices(numbers, 2)
print(f"Indices of 2: {indices}")

# Pattern 3: Chunking a list
def chunk_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

numbers = list(range(10))
chunks = chunk_list(numbers, 3)
print(f"Chunked list: {chunks}")

print("---")

# ---------------------------------------------
# SUMMARY:
# - Lists are ordered, mutable sequences
# - Use [] for creation, list() for conversion
# - Access elements with indexing and slicing
# - Methods: append, extend, insert, remove, pop, sort, reverse
# - List comprehensions for concise transformations
# - Be careful with shallow vs deep copying
# - Lists can be used as stacks and queues
# - Use append() for efficient element addition
# - Lists are versatile for various data structures