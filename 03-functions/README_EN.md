# Python Functions - Learning Materials

This directory covers Python functions in depth, from basic function definitions to advanced concepts like lambda functions and functional programming.

## 📁 Files Overview

### [functions_intro.py](functions_intro.py)
- Basic function definition and calling
- Function parameters and arguments
- Return values and multiple returns
- Default parameters and keyword arguments
- Variable scope (local vs global)
- Functions as first-class objects
- Docstrings and function documentation
- Type hints for better code clarity
- Practical examples:
  - Temperature converters
  - Grade calculator
  - Palindrome checker
  - Fibonacci generator

### [arguments_params.py](arguments_params.py)
- Positional arguments
- Keyword arguments
- Default parameters
- Variable-length arguments (*args, **kwargs)
- Argument unpacking (* and ** operators)
- Keyword-only arguments (after *)
- Positional-only arguments (before /)
- Combining all argument types
- Practical patterns:
  - Configurable logger
  - Flexible shopping cart
  - Database query builder
  - Function decorators with arguments

### [lambda_functions.py](lambda_functions.py)
- Lambda function syntax and basics
- Comparison with regular functions
- Using lambda with built-in functions:
  - `map()`, `filter()`, `sorted()`, `reduce()`
- Lambda with conditional expressions
- Lambda in data processing and sorting
- Lambda with multiple parameters
- Practical applications:
  - Simple calculator
  - Text processing
  - Mathematical operations
  - Data validation
  - Custom sorting
- Limitations and best practices

## 🎯 Learning Objectives
- Understand function definition and invocation
- Master different types of parameters and arguments
- Learn to use return values effectively
- Understand variable scope and lifetime
- Apply lambda functions for concise code
- Use functional programming techniques
- Write modular and reusable code
- Document functions properly with docstrings

## 💡 Key Concepts
- **Functions** are reusable blocks of code that perform specific tasks
- **Parameters** are variables in function definition, **arguments** are actual values passed
- **\*args** collects extra positional arguments as a tuple
- **\*kwargs** collects extra keyword arguments as a dictionary
- **Lambda functions** are anonymous, single-expression functions
- **First-class functions** can be assigned to variables, passed as arguments, and returned from other functions
- **Scope** determines where variables can be accessed

## 🚀 Best Practices
- Use descriptive function names with verbs
- Keep functions small and focused on one task
- Use type hints for better code documentation
- Write comprehensive docstrings
- Prefer keyword arguments for clarity
- Use lambda functions judiciously for simple operations
- Test functions with different argument combinations

## 🔧 Practical Applications
- Code organization and modularization
- Reducing code duplication
- Building reusable utilities
- Data processing pipelines
- Configuration handling
- Decorator patterns
- Functional programming paradigms