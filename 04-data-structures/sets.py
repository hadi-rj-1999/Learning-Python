# ---------------------------------------------------
# Python Sets
# ---------------------------------------------------
# Sets are unordered, mutable collections of unique elements.
# They cannot contain duplicate items.
# Sets are defined using curly braces {} or the set() constructor.
# ---------------------------------------------------

# ---------------------------------------------
# SET CREATION
# ---------------------------------------------
# Empty set (must use set(), not {})
empty_set = set()
print(f"Empty set: {empty_set}")

# Set with elements
fruits = {"apple", "banana", "cherry"}
print(f"Fruits set: {fruits}")

# Set from list (removes duplicates)
numbers = set([1, 2, 3, 2, 1, 4, 5])
print(f"Numbers from list: {numbers}")

# Set from string (creates set of characters)
chars = set("hello")
print(f"Chars from string: {chars}")

# Set with mixed data types
mixed_set = {1, "hello", 3.14, True}
print(f"Mixed set: {mixed_set}")

print("---")

# ---------------------------------------------
# SET PROPERTIES
# ---------------------------------------------
# Sets are unordered
unordered_set = {"a", "b", "c", "d"}
print(f"Unordered set: {unordered_set}")  # Order may vary

# Sets contain only unique elements
duplicates = {1, 2, 2, 3, 3, 3, 4}
print(f"After removing duplicates: {duplicates}")

# Sets cannot contain mutable objects
# This would cause an error:
# invalid_set = {[1, 2], [3, 4]}  # TypeError: unhashable type: 'list'

# But tuples are allowed (immutable)
valid_set = {(1, 2), (3, 4)}
print(f"Set with tuples: {valid_set}")

print("---")

# ---------------------------------------------
# SET OPERATIONS - MATHEMATICAL
# ---------------------------------------------
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(f"Set A: {A}")
print(f"Set B: {B}")

# Union - elements in A or B or both
union = A | B
print(f"Union (A | B): {union}")

# Intersection - elements in both A and B
intersection = A & B
print(f"Intersection (A & B): {intersection}")

# Difference - elements in A but not in B
difference = A - B
print(f"Difference (A - B): {difference}")

# Symmetric Difference - elements in A or B but not both
symmetric_diff = A ^ B
print(f"Symmetric Difference (A ^ B): {symmetric_diff}")

print("---")

# ---------------------------------------------
# SET METHODS - ADDING AND REMOVING
# ---------------------------------------------
colors = {"red", "green"}

# add() - add single element
colors.add("blue")
print(f"After add('blue'): {colors}")

# update() - add multiple elements
colors.update(["yellow", "purple", "orange"])
print(f"After update(): {colors}")

# remove() - remove element (raises error if not found)
colors.remove("green")
print(f"After remove('green'): {colors}")

# discard() - remove element (no error if not found)
colors.discard("pink")  # No error even though pink doesn't exist
colors.discard("red")
print(f"After discard(): {colors}")

# pop() - remove and return arbitrary element
popped = colors.pop()
print(f"Popped: {popped}")
print(f"After pop(): {colors}")

# clear() - remove all elements
colors.clear()
print(f"After clear(): {colors}")

print("---")

# ---------------------------------------------
# SET METHODS - MATHEMATICAL OPERATIONS
# ---------------------------------------------
X = {1, 2, 3, 4}
Y = {3, 4, 5, 6}

# union() method
union_method = X.union(Y)
print(f"X.union(Y): {union_method}")

# intersection() method
intersection_method = X.intersection(Y)
print(f"X.intersection(Y): {intersection_method}")

# difference() method
difference_method = X.difference(Y)
print(f"X.difference(Y): {difference_method}")

# symmetric_difference() method
symmetric_diff_method = X.symmetric_difference(Y)
print(f"X.symmetric_difference(Y): {symmetric_diff_method}")

print("---")

# ---------------------------------------------
# SET METHODS - BOOLEAN OPERATIONS
# ---------------------------------------------
set1 = {1, 2, 3}
set2 = {1, 2}
set3 = {4, 5}

# issubset() - all elements of set2 in set1?
print(f"set2.issubset(set1): {set2.issubset(set1)}")
print(f"set2 <= set1: {set2 <= set1}")

# issuperset() - set1 contains all elements of set2?
print(f"set1.issuperset(set2): {set1.issuperset(set2)}")
print(f"set1 >= set2: {set1 >= set2}")

# isdisjoint() - no common elements?
print(f"set1.isdisjoint(set3): {set1.isdisjoint(set3)}")
print(f"set2.isdisjoint(set3): {set2.isdisjoint(set3)}")

print("---")

# ---------------------------------------------
# SET COMPREHENSIONS
# ---------------------------------------------
# Basic set comprehension
squares = {x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# With condition
even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# From string with condition
vowels = {char for char in "hello world" if char in "aeiou"}
print(f"Vowels in 'hello world': {vowels}")

# Removing duplicates while transforming
words = ["hello", "world", "hello", "python", "world"]
unique_lengths = {len(word) for word in words}
print(f"Unique word lengths: {unique_lengths}")

print("---")

# ---------------------------------------------
# SET OPERATIONS WITH METHODS
# ---------------------------------------------
A = {1, 2, 3}
B = {3, 4, 5}

# Update sets in-place
A.update(B)  # A becomes A | B
print(f"A after update(B): {A}")

A = {1, 2, 3}  # Reset
A.intersection_update(B)  # A becomes A & B
print(f"A after intersection_update(B): {A}")

A = {1, 2, 3}  # Reset
A.difference_update(B)  # A becomes A - B
print(f"A after difference_update(B): {A}")

A = {1, 2, 3}  # Reset
A.symmetric_difference_update(B)  # A becomes A ^ B
print(f"A after symmetric_difference_update(B): {A}")

print("---")

# ---------------------------------------------
# FROZENSET - IMMUTABLE SETS
# ---------------------------------------------
# Creating frozenset
frozen = frozenset([1, 2, 3, 2, 1])
print(f"Frozenset: {frozen}")
print(f"Type: {type(frozen)}")

# Frozenset operations (return new frozensets)
f1 = frozenset([1, 2, 3])
f2 = frozenset([3, 4, 5])

print(f"f1 | f2: {f1 | f2}")
print(f"f1 & f2: {f1 & f2}")
print(f"f1 - f2: {f1 - f2}")

# Frozensets can be used as dictionary keys
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([4, 5, 6])
frozen_dict = {fs1: "first", fs2: "second"}
print(f"Dictionary with frozenset keys: {frozen_dict}")

print("---")

# ---------------------------------------------
# PRACTICAL EXAMPLES
# ---------------------------------------------

# Example 1: Removing duplicates from list
def remove_duplicates(lst):
    """Remove duplicates from a list using set"""
    return list(set(lst))

numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 4, 5, 1]
unique_numbers = remove_duplicates(numbers_with_duplicates)
print(f"Original: {numbers_with_duplicates}")
print(f"Unique: {unique_numbers}")

print("---")

# Example 2: Finding common elements
def find_common_courses(students_courses):
    """Find courses that all students have in common"""
    if not students_courses:
        return set()
    
    common_courses = set(students_courses[0])
    for courses in students_courses[1:]:
        common_courses &= set(courses)
    
    return common_courses

student1 = ["Math", "Physics", "Chemistry", "Biology"]
student2 = ["Math", "Physics", "Computer Science"]
student3 = ["Math", "Physics", "History"]

common = find_common_courses([student1, student2, student3])
print(f"Common courses: {common}")

print("---")

# Example 3: Membership testing performance
import time

# Large list vs set membership test
large_list = list(range(1000000))
large_set = set(large_list)

# Test element at beginning
start = time.time()
result = 0 in large_list
list_time = time.time() - start

start = time.time()
result = 0 in large_set
set_time = time.time() - start

print(f"List membership test: {list_time:.6f} seconds")
print(f"Set membership test: {set_time:.6f} seconds")
print(f"Set is {list_time/set_time:.0f}x faster for membership test")

print("---")

# Example 4: Tag system
class TagSystem:
    def __init__(self):
        self.tags = set()
    
    def add_tags(self, *new_tags):
        self.tags.update(new_tags)
    
    def remove_tags(self, *tags_to_remove):
        self.tags.difference_update(tags_to_remove)
    
    def has_any_tag(self, *search_tags):
        return bool(self.tags & set(search_tags))
    
    def has_all_tags(self, *search_tags):
        return set(search_tags).issubset(self.tags)
    
    def get_common_tags(self, other_system):
        return self.tags & other_system.tags

# Usage
system1 = TagSystem()
system1.add_tags("python", "programming", "tutorial", "beginner")

system2 = TagSystem()
system2.add_tags("python", "advanced", "optimization")

print(f"System1 tags: {system1.tags}")
print(f"System2 tags: {system2.tags}")
print(f"Common tags: {system1.get_common_tags(system2)}")
print(f"System1 has 'python': {system1.has_any_tag('python')}")
print(f"System1 has all 'python','programming': {system1.has_all_tags('python', 'programming')}")

print("---")

# Example 5: Data validation with sets
def validate_data(data, allowed_values):
    """Validate that all data values are in allowed set"""
    invalid_values = set(data) - allowed_values
    if invalid_values:
        return False, invalid_values
    return True, set()

allowed_colors = {"red", "green", "blue", "yellow", "black", "white"}
user_colors = ["red", "green", "purple", "blue"]

is_valid, invalid = validate_data(user_colors, allowed_colors)
print(f"User colors: {user_colors}")
print(f"Allowed colors: {allowed_colors}")
print(f"Valid: {is_valid}")
if not is_valid:
    print(f"Invalid colors: {invalid}")

print("---")

# Example 6: Finding unique characters in text
def analyze_text(text):
    """Analyze unique characters in text"""
    all_chars = set(text)
    letters = {char for char in all_chars if char.isalpha()}
    digits = {char for char in all_chars if char.isdigit()}
    punctuation = {char for char in all_chars if not char.isalnum() and not char.isspace()}
    whitespace = {char for char in all_chars if char.isspace()}
    
    return {
        "all_chars": all_chars,
        "letters": letters,
        "digits": digits,
        "punctuation": punctuation,
        "whitespace": whitespace
    }

sample_text = "Hello World! 123. How are you?"
analysis = analyze_text(sample_text)

print(f"Text: '{sample_text}'")
print(f"All unique chars: {analysis['all_chars']}")
print(f"Letters: {analysis['letters']}")
print(f"Digits: {analysis['digits']}")
print(f"Punctuation: {analysis['punctuation']}")
print(f"Whitespace: {analysis['whitespace']}")

print("---")

# Example 7: Set operations for database-like queries
products = [
    {"id": 1, "name": "Laptop", "tags": {"electronics", "computers", "portable"}},
    {"id": 2, "name": "Book", "tags": {"education", "entertainment"}},
    {"id": 3, "name": "Phone", "tags": {"electronics", "portable", "communication"}},
    {"id": 4, "name": "Desk", "tags": {"furniture", "office"}},
    {"id": 5, "name": "Tablet", "tags": {"electronics", "portable", "entertainment"}}
]

def find_products_by_tags(products, required_tags=None, any_tags=None, exclude_tags=None):
    """Find products based on tag criteria"""
    required_tags = set(required_tags or [])
    any_tags = set(any_tags or [])
    exclude_tags = set(exclude_tags or [])
    
    results = []
    for product in products:
        tags = product["tags"]
        
        # Check required tags (must have all)
        if required_tags and not required_tags.issubset(tags):
            continue
        
        # Check any tags (must have at least one)
        if any_tags and tags.isdisjoint(any_tags):
            continue
        
        # Check exclude tags (must have none)
        if exclude_tags and not tags.isdisjoint(exclude_tags):
            continue
        
        results.append(product)
    
    return results

print("Electronics that are portable:")
electronics_portable = find_products_by_tags(
    products, 
    required_tags=["electronics", "portable"]
)
for product in electronics_portable:
    print(f"  {product['name']}: {product['tags']}")

print("\nProducts with entertainment or education tags:")
entertainment_edu = find_products_by_tags(
    products,
    any_tags=["entertainment", "education"]
)
for product in entertainment_edu:
    print(f"  {product['name']}: {product['tags']}")

print("\nElectronics that are NOT portable:")
electronics_not_portable = find_products_by_tags(
    products,
    required_tags=["electronics"],
    exclude_tags=["portable"]
)
for product in electronics_not_portable:
    print(f"  {product['name']}: {product['tags']}")

print("---")

# ---------------------------------------------
# SET PERFORMANCE CHARACTERISTICS
# ---------------------------------------------
"""
Set Performance:
- Membership testing: O(1) average case
- Adding elements: O(1) average case
- Removing elements: O(1) average case
- Union/Intersection: O(n) where n is size of sets
- Memory: More efficient than lists for large collections

Use sets when:
- You need to check membership frequently
- You need to remove duplicates
- You need mathematical set operations
- Order doesn't matter

Avoid sets when:
- You need to maintain insertion order
- You need to access elements by index
- You have very small collections where overhead isn't worth it
"""

# ---------------------------------------------
# COMMON SET PATTERNS
# ---------------------------------------------

# Pattern 1: Counting unique items
def count_unique(items):
    return len(set(items))

words = ["apple", "banana", "apple", "cherry", "banana", "date"]
print(f"Unique words count: {count_unique(words)}")

# Pattern 2: Finding elements in one set but not another
def find_missing(expected, actual):
    return set(expected) - set(actual)

expected_items = ["A", "B", "C", "D"]
actual_items = ["A", "B", "D"]
missing = find_missing(expected_items, actual_items)
print(f"Missing items: {missing}")

# Pattern 3: Symmetric difference for finding changes
def find_changes(old, new):
    return set(old) ^ set(new)

old_list = [1, 2, 3, 4]
new_list = [1, 3, 5, 6]
changes = find_changes(old_list, new_list)
print(f"Changes between lists: {changes}")

print("---")

# ---------------------------------------------
# SUMMARY:
# - Sets store unique, unordered elements
# - Use {} for non-empty sets, set() for empty sets
# - Mathematical operations: union, intersection, difference, symmetric difference
# - Methods: add, remove, discard, pop, clear, update, etc.
# - Set comprehensions for creating sets from expressions
# - Frozensets are immutable versions of sets
# - Excellent for membership testing and duplicate removal
# - Use when order doesn't matter and uniqueness is important
# - Much faster than lists for membership testing