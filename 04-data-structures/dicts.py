# ---------------------------------------------------
# Python Dictionaries
# ---------------------------------------------------
# Dictionaries are unordered, mutable collections of key-value pairs.
# Keys must be unique and immutable (strings, numbers, tuples).
# Values can be any data type.
# Dictionaries are defined using curly braces {} or the dict() constructor.
# ---------------------------------------------------

# ---------------------------------------------
# DICTIONARY CREATION
# ---------------------------------------------
# Empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")

# Dictionary with key-value pairs
person = {
    "name": "Hadi",
    "age": 26,
    "city": "Mashhad",
    "is_student": False
}
print(f"Person dictionary: {person}")

# Using dict() constructor
from_pairs = dict([("name", "Alice"), ("age", 30), ("city", "Tehran")])
print(f"From pairs: {from_pairs}")

# Using keyword arguments
from_kwargs = dict(name="Bob", age=25, city="Shiraz")
print(f"From kwargs: {from_kwargs}")

# Dictionary with different key types
mixed_keys = {
    "string_key": "value1",
    123: "value2",  # integer key
    (1, 2): "value3",  # tuple key
    True: "value4"  # boolean key
}
print(f"Mixed keys: {mixed_keys}")

print("---")

# ---------------------------------------------
# ACCESSING DICTIONARY ELEMENTS
# ---------------------------------------------
student = {
    "name": "Ali",
    "age": 20,
    "major": "Computer Science",
    "grades": [85, 92, 78]
}

# Access using square brackets
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")

# Access using get() method (safer)
print(f"Major: {student.get('major')}")
print(f"GPA: {student.get('gpa')}")  # Returns None if key doesn't exist
print(f"GPA with default: {student.get('gpa', 'Not available')}")

# Check if key exists
print(f"Has 'name': {'name' in student}")
print(f"Has 'gpa': {'gpa' in student}")

# Get all keys, values, and items
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

print("---")

# ---------------------------------------------
# MODIFYING DICTIONARIES
# ---------------------------------------------
car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020
}

print(f"Original: {car}")

# Adding new key-value pair
car["color"] = "blue"
print(f"After adding color: {car}")

# Modifying existing value
car["year"] = 2022
print(f"After updating year: {car}")

# Using update() to add multiple pairs
car.update({"price": 25000, "fuel": "hybrid"})
print(f"After update: {car}")

# Using setdefault() - returns value if key exists, else sets default
model = car.setdefault("model", "Unknown")
new_feature = car.setdefault("sunroof", False)
print(f"Model: {model}")
print(f"Sunroof: {new_feature}")
print(f"After setdefault: {car}")

print("---")

# ---------------------------------------------
# REMOVING ELEMENTS
# ---------------------------------------------
inventory = {
    "apples": 10,
    "bananas": 15,
    "oranges": 8,
    "grapes": 20,
    "pears": 12
}

print(f"Original inventory: {inventory}")

# pop() - remove by key and return value
apples_count = inventory.pop("apples")
print(f"Removed apples: {apples_count}")
print(f"After pop: {inventory}")

# popitem() - remove and return last inserted item (Python 3.7+)
last_item = inventory.popitem()
print(f"Removed last item: {last_item}")
print(f"After popitem: {inventory}")

# del statement
del inventory["bananas"]
print(f"After del: {inventory}")

# clear() - remove all items
inventory.clear()
print(f"After clear: {inventory}")

print("---")

# ---------------------------------------------
# DICTIONARY METHODS
# ---------------------------------------------
data = {"a": 1, "b": 2, "c": 3, "d": 4}

# copy() - shallow copy
data_copy = data.copy()
print(f"Original: {data}")
print(f"Copy: {data_copy}")

# fromkeys() - create dict from sequence of keys
keys = ["name", "age", "city"]
default_dict = dict.fromkeys(keys, "unknown")
print(f"From keys: {default_dict}")

# items(), keys(), values() - view objects
print(f"Items view: {data.items()}")
print(f"Keys view: {data.keys()}")
print(f"Values view: {data.values()}")

# The view objects are dynamic
data["e"] = 5
print(f"Keys after adding 'e': {list(data.keys())}")

print("---")

# ---------------------------------------------
# DICTIONARY COMPREHENSIONS
# ---------------------------------------------
# Basic comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# With condition
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Transforming existing dictionary
original = {"a": 1, "b": 2, "c": 3}
doubled = {k: v * 2 for k, v in original.items()}
print(f"Doubled: {doubled}")

# Swapping keys and values
swapped = {v: k for k, v in original.items()}
print(f"Swapped: {swapped}")

# Creating dictionary from two lists
keys = ["name", "age", "city"]
values = ["Hadi", 26, "Mashhad"]
person_dict = {k: v for k, v in zip(keys, values)}
print(f"From two lists: {person_dict}")

print("---")

# ---------------------------------------------
# NESTED DICTIONARIES
# ---------------------------------------------
# Dictionary with dictionary values
students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "grades": {"math": 85, "science": 92, "english": 78}
    },
    "student2": {
        "name": "Bob",
        "age": 21,
        "grades": {"math": 90, "science": 88, "english": 95}
    },
    "student3": {
        "name": "Charlie",
        "age": 19,
        "grades": {"math": 76, "science": 82, "english": 80}
    }
}

print("Nested dictionary:")
for student_id, info in students.items():
    print(f"  {student_id}: {info['name']}, Age: {info['age']}")
    print(f"    Grades: {info['grades']}")

# Accessing nested values
alice_math = students["student1"]["grades"]["math"]
print(f"Alice's math grade: {alice_math}")

# Modifying nested values
students["student1"]["grades"]["math"] = 90
print(f"After update: {students['student1']['grades']}")

print("---")

# ---------------------------------------------
# MERGING DICTIONARIES
# ---------------------------------------------
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}  # Note: 'b' exists in both

# Using update() - modifies dict1 in place
dict1.update(dict2)
print(f"After update (dict1): {dict1}")

# Using ** unpacking (Python 3.5+)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {**dict1, **dict2}  # Later dicts override earlier ones
print(f"Merged with **: {merged}")

# Using | operator (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_operator = dict1 | dict2
print(f"Merged with |: {merged_operator}")

print("---")

# ---------------------------------------------
# DICTIONARY ITERATION
# ---------------------------------------------
inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 25,
    "grapes": 40
}

print("Inventory items:")
# Iterate over keys
for key in inventory:
    print(f"  Key: {key}")

print("\nKey-value pairs:")
# Iterate over items
for key, value in inventory.items():
    print(f"  {key}: {value}")

print("\nJust values:")
# Iterate over values
for value in inventory.values():
    print(f"  Value: {value}")

print("\nWith enumeration:")
# With enumeration
for i, (key, value) in enumerate(inventory.items()):
    print(f"  {i+1}. {key}: {value}")

print("---")

# ---------------------------------------------
# DEFAULTDICT (Collections Module)
# ---------------------------------------------
from collections import defaultdict

# Defaultdict with list as default factory
list_default = defaultdict(list)
list_default["fruits"].append("apple")
list_default["fruits"].append("banana")
list_default["vegetables"].append("carrot")
print(f"Defaultdict (list): {dict(list_default)}")

# Defaultdict with int as default factory
int_default = defaultdict(int)
int_default["apples"] += 5
int_default["bananas"] += 3
print(f"Defaultdict (int): {dict(int_default)}")

# Defaultdict with custom default factory
def default_value():
    return "unknown"

custom_default = defaultdict(default_value)
custom_default["name"] = "Hadi"
print(f"Name: {custom_default['name']}")
print(f"Age: {custom_default['age']}")  # Returns "unknown"
print(f"City: {custom_default['city']}")  # Returns "unknown"

print("---")

# ---------------------------------------------
# ORDEREDDICT (Collections Module)
# ---------------------------------------------
from collections import OrderedDict

# OrderedDict maintains insertion order
ordered = OrderedDict()
ordered["first"] = 1
ordered["second"] = 2
ordered["third"] = 3
ordered["fourth"] = 4

print("OrderedDict:")
for key, value in ordered.items():
    print(f"  {key}: {value}")

# Moving items to end
ordered.move_to_end("first")
print(f"After move_to_end: {dict(ordered)}")

# Regular dict also maintains order in Python 3.7+
regular_dict = {"first": 1, "second": 2, "third": 3}
print(f"Regular dict (also ordered): {regular_dict}")

print("---")

# ---------------------------------------------
# COUNTER (Collections Module)
# ---------------------------------------------
from collections import Counter

# Count occurrences
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = Counter(words)
print(f"Word counts: {word_count}")

# Most common elements
print(f"Most common: {word_count.most_common(2)}")

# Counter operations
counter1 = Counter(a=3, b=2, c=1)
counter2 = Counter(a=1, b=2, c=3, d=4)

print(f"Counter1: {counter1}")
print(f"Counter2: {counter2}")
print(f"Addition: {counter1 + counter2}")
print(f"Subtraction: {counter1 - counter2}")
print(f"Intersection: {counter1 & counter2}")
print(f"Union: {counter1 | counter2}")

print("---")

# ---------------------------------------------
# PRACTICAL EXAMPLES
# ---------------------------------------------

# Example 1: Student Gradebook
gradebook = {
    "Alice": {
        "math": 85,
        "science": 92,
        "english": 78,
        "history": 88
    },
    "Bob": {
        "math": 90,
        "science": 88,
        "english": 95,
        "history": 82
    },
    "Charlie": {
        "math": 76,
        "science": 82,
        "english": 80,
        "history": 79
    }
}

def calculate_averages(gradebook):
    """Calculate average grade for each student"""
    averages = {}
    for student, grades in gradebook.items():
        average = sum(grades.values()) / len(grades)
        averages[student] = round(average, 2)
    return averages

def find_top_student(gradebook, subject):
    """Find student with highest grade in a subject"""
    top_student = None
    top_grade = -1
    
    for student, grades in gradebook.items():
        if grades[subject] > top_grade:
            top_grade = grades[subject]
            top_student = student
    
    return top_student, top_grade

averages = calculate_averages(gradebook)
print("Student averages:")
for student, avg in averages.items():
    print(f"  {student}: {avg}")

top_math_student, math_grade = find_top_student(gradebook, "math")
print(f"Top math student: {top_math_student} with {math_grade}")

print("---")

# Example 2: Word Frequency Counter
def word_frequency(text):
    """Count frequency of each word in text"""
    words = text.lower().split()
    frequency = {}
    
    for word in words:
        # Remove punctuation
        word = word.strip('.,!?;:"')
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    
    return frequency

sample_text = "Hello world! Hello Python. Python is great. World says hello to Python."
freq = word_frequency(sample_text)

print("Word frequencies:")
for word, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    print(f"  {word}: {count}")

print("---")

# Example 3: Configuration Management
class Config:
    def __init__(self, defaults=None):
        self._config = defaults or {}
    
    def set(self, key, value):
        """Set configuration value"""
        keys = key.split('.')
        current = self._config
        
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        
        current[keys[-1]] = value
    
    def get(self, key, default=None):
        """Get configuration value"""
        keys = key.split('.')
        current = self._config
        
        for k in keys:
            if k not in current:
                return default
            current = current[k]
        
        return current
    
    def __str__(self):
        return str(self._config)

# Usage
config = Config({
    "database": {
        "host": "localhost",
        "port": 5432
    },
    "app": {
        "name": "MyApp",
        "debug": True
    }
})

config.set("database.user", "admin")
config.set("app.features.export", True)

print("Configuration:")
print(f"  Database host: {config.get('database.host')}")
print(f"  Database user: {config.get('database.user')}")
print(f"  App debug: {config.get('app.debug')}")
print(f"  Export feature: {config.get('app.features.export')}")
print(f"  Full config: {config}")

print("---")

# Example 4: Cache Implementation
class SimpleCache:
    def __init__(self, max_size=100):
        self.cache = {}
        self.max_size = max_size
        self.access_order = []
    
    def get(self, key):
        """Get value from cache"""
        if key in self.cache:
            # Move to end (most recently used)
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache[key]
        return None
    
    def set(self, key, value):
        """Set value in cache"""
        if len(self.cache) >= self.max_size:
            # Remove least recently used
            lru_key = self.access_order.pop(0)
            del self.cache[lru_key]
        
        self.cache[key] = value
        self.access_order.append(key)
    
    def __str__(self):
        return str({k: self.cache[k] for k in self.access_order})

# Usage
cache = SimpleCache(max_size=3)
cache.set("user:1", "Alice")
cache.set("user:2", "Bob")
cache.set("user:3", "Charlie")

print("Cache contents:")
print(f"  {cache}")

# Access user:1 to make it most recent
cache.get("user:1")
cache.set("user:4", "Diana")  # This should remove user:2 (least recent)

print("After adding user:4:")
print(f"  {cache}")

print("---")

# Example 5: Data Transformation
def transform_data(rows, key_field):
    """Transform list of dictionaries to dictionary keyed by field"""
    transformed = {}
    
    for row in rows:
        key = row[key_field]
        transformed[key] = row
    
    return transformed

# Sample data
employees = [
    {"id": 1, "name": "Alice", "department": "Engineering", "salary": 75000},
    {"id": 2, "name": "Bob", "department": "Marketing", "salary": 65000},
    {"id": 3, "name": "Charlie", "department": "Engineering", "salary": 80000},
    {"id": 4, "name": "Diana", "department": "HR", "salary": 60000}
]

# Transform by ID
by_id = transform_data(employees, "id")
print("Employees by ID:")
for emp_id, emp_data in by_id.items():
    print(f"  {emp_id}: {emp_data['name']} - {emp_data['department']}")

# Group by department
from collections import defaultdict
by_department = defaultdict(list)
for emp in employees:
    by_department[emp["department"]].append(emp)

print("\nEmployees by department:")
for dept, dept_employees in by_department.items():
    print(f"  {dept}: {[emp['name'] for emp in dept_employees]}")

print("---")

# ---------------------------------------------
# DICTIONARY PERFORMANCE
# ---------------------------------------------
"""
Dictionary Performance:
- Average case time complexity:
  - Access: O(1)
  - Insert: O(1)
  - Delete: O(1)
  - Search: O(1)

- Worst case (with many collisions): O(n)

Memory overhead is higher than lists due to hash table structure.
"""

# Performance comparison: list vs dict membership test
import time

large_list = list(range(1000000))
large_dict = {i: i for i in range(1000000)}

# Test membership
test_value = 999999

start = time.time()
result = test_value in large_list
list_time = time.time() - start

start = time.time()
result = test_value in large_dict
dict_time = time.time() - start

print(f"List membership test: {list_time:.6f} seconds")
print(f"Dict membership test: {dict_time:.6f} seconds")
print(f"Dictionary is {list_time/dict_time:.0f}x faster for membership")

print("---")

# ---------------------------------------------
# COMMON PATTERNS AND IDIOMS
# ---------------------------------------------

# Pattern 1: Grouping with defaultdict
def group_by_key(items, key_func):
    """Group items by a key function"""
    grouped = defaultdict(list)
    for item in items:
        key = key_func(item)
        grouped[key].append(item)
    return dict(grouped)

# Example: Group numbers by even/odd
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
grouped = group_by_key(numbers, lambda x: "even" if x % 2 == 0 else "odd")
print(f"Grouped numbers: {grouped}")

# Pattern 2: Dictionary as switch statement
def handle_operation(operation, a, b):
    """Use dictionary as switch/case alternative"""
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else "Error"
    }
    
    handler = operations.get(operation)
    if handler:
        return handler(a, b)
    else:
        return "Unknown operation"

print(f"5 + 3 = {handle_operation('add', 5, 3)}")
print(f"10 / 2 = {handle_operation('divide', 10, 2)}")

# Pattern 3: Inverting a dictionary
def invert_dict(d):
    """Invert a dictionary (values become keys)"""
    inverted = {}
    for key, value in d.items():
        if value not in inverted:
            inverted[value] = []
        inverted[value].append(key)
    return inverted

original = {"a": 1, "b": 2, "c": 1, "d": 3}
inverted = invert_dict(original)
print(f"Original: {original}")
print(f"Inverted: {inverted}")

print("---")

# ---------------------------------------------
# SUMMARY:
# - Dictionaries store key-value pairs
# - Keys must be immutable, values can be anything
# - Access with [] or get() method
# - Methods: keys(), values(), items(), update(), pop(), etc.
# - Dictionary comprehensions for transformation
# - Nested dictionaries for complex data
# - Collections module: defaultdict, OrderedDict, Counter
# - Excellent for fast lookups and data organization
# - Use when you need to associate data with unique identifiers