# ---------------------------------------------------
# Python For Loops
# ---------------------------------------------------
# For loops are used for iterating over sequences 
# (list, tuple, string, dictionary, set, etc.)
# or any iterable object.
# ---------------------------------------------------

# ---------------------------------------------
# BASIC FOR LOOP WITH LIST
# ---------------------------------------------
fruits = ["apple", "banana", "cherry", "orange"]
for fruit in fruits:
    print(fruit)

print("---")

# ---------------------------------------------
# FOR LOOP WITH STRING
# ---------------------------------------------
word = "Python"
for letter in word:
    print(letter)

print("---")

# ---------------------------------------------
# FOR LOOP WITH RANGE()
# ---------------------------------------------
# range(stop) → 0 to stop-1
for i in range(5):
    print(i)

print("---")

# range(start, stop) → start to stop-1
for i in range(2, 6):
    print(i)

print("---")

# range(start, stop, step) → start to stop-1 with step
for i in range(0, 10, 2):
    print(i)

print("---")

# Counting backwards
for i in range(5, 0, -1):
    print(i)

print("---")

# ---------------------------------------------
# FOR LOOP WITH TUPLE
# ---------------------------------------------
colors = ("red", "green", "blue", "yellow")
for color in colors:
    print(color.upper())

print("---")

# ---------------------------------------------
# FOR LOOP WITH DICTIONARY
# ---------------------------------------------
student = {
    "name": "Hadi",
    "age": 26,
    "city": "Mashhad",
    "grade": "A"
}

# Looping through keys
for key in student:
    print(f"Key: {key}")

print("---")

# Looping through keys explicitly
for key in student.keys():
    print(f"Key: {key}")

print("---")

# Looping through values
for value in student.values():
    print(f"Value: {value}")

print("---")

# Looping through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")

print("---")

# ---------------------------------------------
# FOR LOOP WITH SET
# ---------------------------------------------
unique_numbers = {1, 3, 5, 3, 7, 5, 9}
for number in unique_numbers:
    print(f"Number: {number}")

print("---")

# ---------------------------------------------
# BREAK STATEMENT
# ---------------------------------------------
# Exit the loop when condition is met
numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number found: {num}")
        break
    print(f"Checking: {num}")

print("---")

# ---------------------------------------------
# CONTINUE STATEMENT
# ---------------------------------------------
# Skip current iteration and continue with next
for i in range(10):
    if i % 2 == 0:  # skip even numbers
        continue
    print(f"Odd number: {i}")

print("---")

# ---------------------------------------------
# ELSE CLAUSE WITH FOR LOOP
# ---------------------------------------------
# The else block executes after the loop finishes normally
# (without hitting a break statement)
for i in range(3):
    print(i)
else:
    print("Loop completed successfully!")

print("---")

# Else doesn't execute when break is used
for i in range(5):
    if i == 3:
        print("Breaking at 3")
        break
    print(i)
else:
    print("This won't print due to break")

print("---")

# ---------------------------------------------
# NESTED FOR LOOPS
# ---------------------------------------------
# Loop inside another loop
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

print("---")

# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i * j}")
    print()  # empty line between tables

print("---")

# ---------------------------------------------
# ENUMERATE() FUNCTION
# ---------------------------------------------
# Get both index and value
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

print("---")

# Start index from specific number
for index, fruit in enumerate(fruits, start=1):
    print(f"#{index}: {fruit}")

print("---")

# ---------------------------------------------
# ZIP() FUNCTION
# ---------------------------------------------
# Iterate over multiple sequences simultaneously
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

print("---")

# ---------------------------------------------
# LIST COMPREHENSION (Advanced but useful)
# ---------------------------------------------
# Create new lists using for loops in one line
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# With condition
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

print("---")

# ---------------------------------------------
# PRACTICAL EXAMPLES
# ---------------------------------------------
# Example 1: Calculate sum of numbers
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Sum of {numbers} = {total}")

# Example 2: Find maximum number
numbers = [3, 7, 2, 9, 1, 5]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Maximum number: {max_num}")

# Example 3: Count characters in string
text = "hello world"
char_count = {}
for char in text:
    if char != " ":  # skip spaces
        char_count[char] = char_count.get(char, 0) + 1
print(f"Character count: {char_count}")

# Example 4: Pattern printing
for i in range(1, 6):
    print("*" * i)

print("---")

# Example 5: Filtering list
numbers = [12, 7, 25, 8, 33, 14, 5]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"Even numbers: {even_numbers}")

# ---------------------------------------------
# SUMMARY:
# - Use for loops to iterate over sequences
# - range() generates number sequences
# - break exits loop, continue skips iteration
# - else executes after normal loop completion
# - enumerate() for index-value pairs
# - zip() for multiple sequences
# - Nested loops for multi-dimensional iteration