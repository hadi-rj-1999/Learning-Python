# ---------------------------------------------------
# Python Break and Continue Statements
# ---------------------------------------------------
# break: exits the current loop entirely
# continue: skips the current iteration and continues with the next
# These statements give you more control over loop execution.
# ---------------------------------------------------

# ---------------------------------------------
# BREAK STATEMENT IN FOR LOOPS
# ---------------------------------------------
print("BREAK IN FOR LOOPS:")
print("-" * 20)

# Exit loop when condition is met
numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number found: {num}")
        break
    print(f"Processing odd number: {num}")

print("---")

# Search for specific item
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
target = "cherry"

for fruit in fruits:
    print(f"Checking: {fruit}")
    if fruit == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found in the list")

print("---")

# ---------------------------------------------
# CONTINUE STATEMENT IN FOR LOOPS
# ---------------------------------------------
print("CONTINUE IN FOR LOOPS:")
print("-" * 20)

# Skip even numbers
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {i}")

print("---")

# Process only valid data
data = [10, 0, 25, -5, 30, 0, 15]
for value in data:
    if value <= 0:
        continue  # Skip invalid values
    print(f"Processing valid value: {value}")

print("---")

# Skip specific items
fruits = ["apple", "banana", "kiwi", "orange", "grape"]
skip_fruits = ["banana", "orange"]

for fruit in fruits:
    if fruit in skip_fruits:
        continue  # Skip unwanted fruits
    print(f"I like {fruit}")

print("---")

# ---------------------------------------------
# BREAK STATEMENT IN WHILE LOOPS
# ---------------------------------------------
print("BREAK IN WHILE LOOPS:")
print("-" * 20)

# Break out of infinite loop
count = 0
while True:
    count += 1
    print(f"Count: {count}")
    if count >= 5:
        break

print("Loop exited with break")
print("---")

# User input with break
# Uncomment to test:
# while True:
#     user_input = input("Enter a number (or 'quit' to exit): ")
#     if user_input == "quit":
#         break
#     print(f"You entered: {user_input}")

# print("Input session ended")
# print("---")

# ---------------------------------------------
# CONTINUE STATEMENT IN WHILE LOOPS
# ---------------------------------------------
print("CONTINUE IN WHILE LOOPS:")
print("-" * 20)

# Skip even numbers in while loop
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(f"Odd: {num}")

print("---")

# Input validation with continue
# Uncomment to test:
# total = 0
# while True:
#     user_input = input("Enter a positive number (or 'done' to finish): ")
#     
#     if user_input == "done":
#         break
#     
#     try:
#         number = float(user_input)
#         if number <= 0:
#             print("Please enter a positive number")
#             continue
#     except ValueError:
#         print("Please enter a valid number")
#         continue
#     
#     total += number
#     print(f"Current total: {total}")

# print(f"Final total: {total}")
# print("---")

# ---------------------------------------------
# BREAK AND CONTINUE IN NESTED LOOPS
# ---------------------------------------------
print("NESTED LOOPS WITH BREAK/CONTINUE:")
print("-" * 20)

# Break only affects inner loop
print("Break in inner loop:")
for i in range(1, 4):
    print(f"Outer loop: i = {i}")
    for j in range(1, 4):
        if j == 2:
            break  # Only breaks inner loop
        print(f"  Inner loop: j = {j}")

print("---")

# Continue in nested loops
print("Continue in inner loop:")
for i in range(1, 4):
    print(f"Outer: {i}")
    for j in range(1, 4):
        if j == 2:
            continue  # Skips only current iteration of inner loop
        print(f"  Inner: {j}")

print("---")

# ---------------------------------------------
# PRACTICAL EXAMPLES
# ---------------------------------------------
print("PRACTICAL EXAMPLES:")
print("-" * 20)

# Example 1: Prime number check
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Find first prime number in a list
numbers = [4, 6, 8, 9, 11, 12, 13]
for num in numbers:
    if is_prime(num):
        print(f"First prime number found: {num}")
        break
else:
    print("No prime numbers found")

print("---")

# Example 2: Data processing with validation
data = [25, "invalid", 30, -5, 42, "error", 15]
valid_numbers = []

for item in data:
    # Skip non-integer values
    if not isinstance(item, int):
        print(f"Skipping non-integer: {item}")
        continue
    
    # Skip negative numbers
    if item < 0:
        print(f"Skipping negative: {item}")
        continue
    
    valid_numbers.append(item)

print(f"Valid numbers: {valid_numbers}")
print("---")

# Example 3: Search with multiple conditions
students = [
    {"name": "Alice", "grade": 85, "attendance": 90},
    {"name": "Bob", "grade": 92, "attendance": 75},
    {"name": "Charlie", "grade": 78, "attendance": 95},
    {"name": "Diana", "grade": 95, "attendance": 98}
]

# Find first student with grade > 90 AND attendance > 80
for student in students:
    print(f"Checking {student['name']}")
    if student["grade"] > 90 and student["attendance"] > 80:
        print(f"Perfect candidate found: {student['name']}")
        print(f"Grade: {student['grade']}, Attendance: {student['attendance']}")
        break
else:
    print("No perfect candidate found")

print("---")

# Example 4: Menu system with break/continue
# Uncomment to test:
# while True:
#     print("\n=== MENU ===")
#     print("1. Option One")
#     print("2. Option Two")
#     print("3. Option Three")
#     print("4. Exit")
#     
#     choice = input("Enter your choice (1-4): ")
#     
#     if choice == "4":
#         print("Goodbye!")
#         break
#     
#     if choice not in ["1", "2", "3"]:
#         print("Invalid choice! Please try again.")
#         continue
#     
#     # Process valid choices
#     if choice == "1":
#         print("You selected Option One")
#     elif choice == "2":
#         print("You selected Option Two")
#     elif choice == "3":
#         print("You selected Option Three")
#     
#     input("Press Enter to continue...")

# Example 5: Skip header row in data processing
data_rows = [
    ["Name", "Age", "City"],  # Header row
    ["Alice", 25, "New York"],
    ["Bob", 30, "London"],
    ["Charlie", 35, "Paris"]
]

print("Processing data (skipping header):")
for row in data_rows:
    if row[0] == "Name":  # Skip header
        continue
    print(f"Name: {row[0]}, Age: {row[1]}, City: {row[2]}")

print("---")

# ---------------------------------------------
# BREAK/CONTINUE WITH ELSE CLAUSE
# ---------------------------------------------
print("BREAK/CONTINUE WITH ELSE:")
print("-" * 20)

# For loop else executes only if no break occurred
numbers = [1, 3, 5, 7, 9]
for num in numbers:
    if num % 2 == 0:
        print(f"Even number found: {num}")
        break
else:
    print("No even numbers found")

print("---")

# While loop else
count = 0
while count < 5:
    if count == 3:
        print("Breaking at 3")
        break
    print(f"Count: {count}")
    count += 1
else:
    print("Loop completed without break")

print("---")

# ---------------------------------------------
# COMMON PATTERNS AND TIPS
# ---------------------------------------------
print("COMMON PATTERNS:")
print("-" * 20)

# Pattern 1: Early exit for efficiency
large_list = list(range(1, 1001))
search_value = 42

for item in large_list:
    if item == search_value:
        print(f"Found {search_value} early!")
        break
    # Without break, we'd check all 1000 items
else:
    print(f"{search_value} not found")

print("---")

# Pattern 2: Skip expensive operations
def expensive_operation(x):
    print(f"Performing expensive operation on {x}")
    return x * 2

data = [1, 0, 3, -2, 5]
results = []

for num in data:
    if num <= 0:
        continue  # Skip expensive operation for invalid data
    result = expensive_operation(num)
    results.append(result)

print(f"Results: {results}")
print("---")

# Pattern 3: Input validation loop
# Uncomment to test:
# while True:
#     age_input = input("Enter your age: ")
#     
#     if not age_input.isdigit():
#         print("Please enter a valid number")
#         continue
#     
#     age = int(age_input)
#     if age < 0 or age > 120:
#         print("Please enter a realistic age (0-120)")
#         continue
#     
#     break  # Valid input received
# 
# print(f"Your age is: {age}")

# ---------------------------------------------
# SUMMARY:
# - break: immediately exits the current loop
# - continue: skips to next iteration of current loop
# - Use break for early termination when condition met
# - Use continue to skip unwanted iterations
# - break in nested loops only exits the innermost loop
# - else clause with loops executes only if no break occurred
# - These statements work in both for and while loops
# - Useful for input validation, searching, and data filtering