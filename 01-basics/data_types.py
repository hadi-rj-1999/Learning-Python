# ---------------------------------------------------
# Python Data Types - Basic Overview
# ---------------------------------------------------
# Python has several built-in data types.
# The most common categories are:
#   - Text Type:      str
#   - Numeric Types:  int, float, complex
#   - Sequence Types: list, tuple, range
#   - Mapping Type:   dict
#   - Set Types:      set, frozenset
#   - Boolean Type:   bool
#   - Binary Types:   bytes, bytearray, memoryview
# ---------------------------------------------------

# ---------------------------------------------
# STRING (str)
# ---------------------------------------------
text_1 = "Hello"
text_2 = 'World'
print(text_1, text_2)
print(type(text_1))

# ---------------------------------------------
# INTEGER (int)
# ---------------------------------------------
age = 26
year = 2025
print(age, year)
print(type(age))

# ---------------------------------------------
# FLOAT (float)
# ---------------------------------------------
price = 19.99
temperature = -4.5
print(price, temperature)
print(type(price))

# ---------------------------------------------
# COMPLEX (complex)
# ---------------------------------------------
z = 3 + 5j
print(z)
print(type(z))

# ---------------------------------------------
# LIST (list)
# ---------------------------------------------
numbers = [1, 2, 3, 4]
fruits = ["apple", "banana", "orange"]
print(numbers, fruits)
print(type(numbers))

# ---------------------------------------------
# TUPLE (tuple)
# ---------------------------------------------
coordinates = (10, 20)
colors = ("red", "green", "blue")
print(coordinates, colors)
print(type(coordinates))

# ---------------------------------------------
# RANGE (range)
# ---------------------------------------------
r = range(5)
print(list(r))
print(type(r))

# ---------------------------------------------
# DICTIONARY (dict)
# ---------------------------------------------
person = {
    "name": "Hadi",
    "age": 26,
    "city": "Mashhad"
}
print(person)
print(type(person))

# ---------------------------------------------
# SET (set)
# ---------------------------------------------
unique_numbers = {1, 2, 3, 3, 2}
print(unique_numbers)  # duplicates removed
print(type(unique_numbers))

# ---------------------------------------------
# FROZENSET (frozenset)
# ---------------------------------------------
immutable_set = frozenset([1, 2, 3])
print(immutable_set)
print(type(immutable_set))

# ---------------------------------------------
# BOOLEAN (bool)
# ---------------------------------------------
is_active = True
is_admin = False
print(is_active, is_admin)
print(type(is_active))

# ---------------------------------------------
# BINARY TYPES
# ---------------------------------------------
byte_data = b"Hello"
byte_array = bytearray(5)
print(byte_data, byte_array)
print(type(byte_data))

# ---------------------------------------------
# Checking type using type()
# ---------------------------------------------
print(type(text_1))
print(type(numbers))
print(type(person))
print(type(unique_numbers))
