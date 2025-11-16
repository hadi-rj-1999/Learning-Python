# ---------------------------------------------
# Python Variables
# ---------------------------------------------

# Python does not have a command to declare variables.
# A variable is created when you assign a value to it.

x = "hello world"
y = 26

print(x)
print(y)

# ---------------------------------------------
# Dynamic Typing
# ---------------------------------------------
# Variables do not need a specific type and can change type at any time.

x = 100        # now x is an integer
y = "my name is hadi"   # now y is a string

print(x)
print(y)

# ---------------------------------------------
# Type Casting (str, int, float)
# ---------------------------------------------
# You can set the type using casting.

var_1 = str(23)   # "23"
var_2 = int(3.14) # 3 → decimal removed
var_3 = float(21) # 21.0

print(var_1, var_2, var_3, sep="\n")

# ---------------------------------------------
# Checking variable type using type()
# ---------------------------------------------

print(type(x))
print(type(y))
print(type(var_1))
print(type(var_2))
print(type(var_3))

# ---------------------------------------------
# Multiple Variable Assignment
# ---------------------------------------------
# Assigning multiple variables in one line:

a, b, c = 5, "apple", 3.14
print(a, b, c)

# Same value to multiple variables:
p = q = r = 10
print(p, q, r)

# ---------------------------------------------
# Variable Naming Rules
# ---------------------------------------------
# 1. Must start with a letter or underscore (_)
# 2. Cannot start with a number
# 3. Can contain letters, numbers, underscores
# 4. Case-sensitive (age, Age are different)
# 5. Use readable names (snake_case recommended)

user_name = "hadi"
number_of_cars = 4
