# ---------------------------------------------------
# Python While Loops
# ---------------------------------------------------
# While loops execute a set of statements as long as 
# a condition is true.
# They are useful when you don't know how many iterations
# you need in advance.
# ---------------------------------------------------

# ---------------------------------------------
# BASIC WHILE LOOP
# ---------------------------------------------
# Simple counter
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1  # Important: don't forget to update the counter!

print("Loop finished!")
print("---")

# ---------------------------------------------
# WHILE LOOP WITH USER INPUT
# ---------------------------------------------
# Example: Ask user until they enter 'quit'
# Uncomment to test:
# user_input = ""
# while user_input != "quit":
#     user_input = input("Enter a word (type 'quit' to exit): ")
#     print(f"You entered: {user_input}")

# print("Game over!")
# print("---")

# ---------------------------------------------
# WHILE LOOP WITH BREAK
# ---------------------------------------------
# Using break to exit loop
number = 0
while True:  # Infinite loop
    number += 1
    print(number)
    if number >= 5:
        break  # Exit the loop

print("Loop broken with break statement")
print("---")

# ---------------------------------------------
# WHILE LOOP WITH CONTINUE
# ---------------------------------------------
# Skip even numbers
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # Skip the rest for even numbers
    print(f"Odd number: {num}")

print("---")

# ---------------------------------------------
# WHILE LOOP WITH ELSE
# ---------------------------------------------
# The else block executes when the condition becomes false
counter = 1
while counter <= 3:
    print(f"Counter: {counter}")
    counter += 1
else:
    print("While loop completed normally")

print("---")

# Else doesn't execute when break is used
counter = 1
while counter <= 5:
    if counter == 3:
        print("Breaking at 3")
        break
    print(f"Counter: {counter}")
    counter += 1
else:
    print("This won't print due to break")

print("---")

# ---------------------------------------------
# NESTED WHILE LOOPS
# ---------------------------------------------
# While loop inside another while loop
i = 1
while i <= 3:
    j = 1
    print(f"Outer loop: i = {i}")
    
    while j <= 2:
        print(f"  Inner loop: j = {j}")
        j += 1
    
    i += 1
    print()  # Empty line for separation

print("---")

# ---------------------------------------------
# PRACTICAL EXAMPLES
# ---------------------------------------------

# Example 1: Number guessing game
# Uncomment to play:
# secret_number = 7
# guess = 0
# attempts = 0
# 
# while guess != secret_number:
#     guess = int(input("Guess a number between 1-10: "))
#     attempts += 1
#     
#     if guess < secret_number:
#         print("Too low! Try again.")
#     elif guess > secret_number:
#         print("Too high! Try again.")
# 
# print(f"Congratulations! You guessed it in {attempts} attempts.")

# Example 2: Fibonacci sequence
print("Fibonacci sequence:")
a, b = 0, 1
count = 0
while count < 10:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

print("\n---")

# Example 3: Factorial calculation
number = 5
factorial = 1
current = 1

while current <= number:
    factorial *= current
    current += 1

print(f"Factorial of {number} is {factorial}")
print("---")

# Example 4: Password validation
# Uncomment to test:
# correct_password = "python123"
# attempts = 3
# 
# while attempts > 0:
#     password = input(f"Enter password ({attempts} attempts left): ")
#     
#     if password == correct_password:
#         print("Access granted!")
#         break
#     else:
#         print("Incorrect password!")
#         attempts -= 1
# else:
#     print("Too many failed attempts. Account locked!")

# Example 5: Simple calculator with menu
# Uncomment to test:
# while True:
#     print("\nSimple Calculator")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")
#     
#     choice = input("Enter your choice (1-5): ")
#     
#     if choice == "5":
#         print("Goodbye!")
#         break
#     
#     if choice in ["1", "2", "3", "4"]:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#         
#         if choice == "1":
#             result = num1 + num2
#             print(f"Result: {num1} + {num2} = {result}")
#         elif choice == "2":
#             result = num1 - num2
#             print(f"Result: {num1} - {num2} = {result}")
#         elif choice == "3":
#             result = num1 * num2
#             print(f"Result: {num1} × {num2} = {result}")
#         elif choice == "4":
#             if num2 != 0:
#                 result = num1 / num2
#                 print(f"Result: {num1} ÷ {num2} = {result}")
#             else:
#                 print("Error: Cannot divide by zero!")
#     else:
#         print("Invalid choice! Please try again.")

# ---------------------------------------------
# COMMON PATTERNS AND IDIOMS
# ---------------------------------------------

# Pattern 1: Input validation
# Uncomment to test:
# age = -1
# while age < 0 or age > 120:
#     try:
#         age = int(input("Enter your age (0-120): "))
#         if age < 0 or age > 120:
#             print("Please enter a valid age between 0 and 120")
#     except ValueError:
#         print("Please enter a valid number")
# 
# print(f"Your age is: {age}")

# Pattern 2: Processing until sentinel value
print("Enter numbers to sum (enter 0 to finish):")
total = 0
# Uncomment to test:
# while True:
#     num = float(input("Enter a number: "))
#     if num == 0:
#         break
#     total += num
# 
# print(f"Total sum: {total}")

# Pattern 3: Decreasing counter with condition
time_remaining = 10
while time_remaining > 0:
    print(f"Time remaining: {time_remaining} seconds")
    time_remaining -= 1
    # In real application, you might have time.sleep(1) here

print("Time's up!")
print("---")

# ---------------------------------------------
# COMPARISON: WHILE vs FOR LOOPS
# ---------------------------------------------
print("While loop example:")
# When you don't know iterations in advance
import random
target = random.randint(1, 100)
guesses = 0
# Simulated guessing
current_guess = 0
while current_guess != target:
    current_guess = random.randint(1, 100)
    guesses += 1

print(f"Found {target} in {guesses} guesses")

print("\nFor loop example:")
# When you know exact iterations
for i in range(1, 6):
    print(f"Number: {i}")

print("---")

# ---------------------------------------------
# POTENTIAL PITFALLS
# ---------------------------------------------

# Pitfall 1: Infinite loops
# WARNING: Don't uncomment this - it will run forever!
# while True:
#     print("This will run forever!")

# Pitfall 2: Forgetting to update counter
# count = 1
# while count <= 5:
#     print(count)
#     # Forgot: count += 1
#     # This creates infinite loop!

# Safe way: Always ensure condition will eventually become false

# ---------------------------------------------
# SUMMARY:
# - Use while loops when iterations are unknown
# - Always update loop variable to avoid infinite loops
# - break exits the loop, continue skips to next iteration
# - else executes when condition becomes false (no break)
# - Useful for menus, games, input validation
# - Be careful of infinite loops!
# - Choose while vs for based on whether you know iterations