
# Python Exception Handling Guide

## Introduction
In Python, an **exception** is an event that occurs during the execution of a program and disrupts its normal flow. 

### **Why are exceptions important?**
- They prevent unexpected crashes.
- They allow error handling without stopping program execution.
- They provide clear debugging information.

---

## **Types of Python Exceptions**

### 1. Base Classes
These are foundational exceptions from which other exceptions are derived.

**Example:**
```python
try:
    raise Exception("This is a general exception")
except Exception as e:
    print(f"Caught an exception: {e}")
```

---

### 2. Arithmetic Exceptions
These exceptions arise from mathematical errors.

**Example - ZeroDivisionError:**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
```

**Example - OverflowError:**
```python
import sys
try:
    result = sys.maxsize * sys.maxsize
except OverflowError:
    print("Error: Numerical result out of range")
```

---

### 3. Lookup Errors
These exceptions occur when an invalid key or index is used.

**Example - IndexError:**
```python
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("Error: List index out of range")
```

**Example - KeyError:**
```python
try:
    data = {"name": "Alice"}
    print(data["age"])
except KeyError:
    print("Error: Key not found in dictionary")
```

---

### 4. Import Errors
These exceptions occur when importing a module fails.

**Example - ImportError:**
```python
try:
    import non_existent_module
except ImportError:
    print("Error: Module not found")
```

---

### 5. Attribute Errors
These occur when an attribute reference or assignment fails.

**Example - AttributeError:**
```python
try:
    number = 42
    number.append(3)
except AttributeError:
    print("Error: 'int' object has no attribute 'append'")
```

---

### 6. File Handling Exceptions
These arise when performing file operations.

**Example - FileNotFoundError:**
```python
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found")
```

**Example - PermissionError:**
```python
try:
    with open("/root/secret.txt", "w") as file:
        file.write("Unauthorized access")
except PermissionError:
    print("Error: Permission denied")
```

---

### 7. Type and Value Errors
These exceptions occur when incorrect data types or values are provided.

**Example - TypeError:**
```python
try:
    result = "5" + 5
except TypeError:
    print("Error: Cannot concatenate string with integer")
```

**Example - ValueError:**
```python
try:
    number = int("abc")
except ValueError:
    print("Error: Invalid value for conversion to int")
```

---

### 8. Runtime Errors
These occur when something goes wrong that doesn't fit into other categories.

**Example - RuntimeError:**
```python
try:
    raise RuntimeError("An unexpected runtime error occurred")
except RuntimeError as e:
    print(f"Error: {e}")
```

---

### 9. Recursion Errors
These happen when maximum recursion depth is exceeded.

**Example - RecursionError:**
```python
def recursive_function():
    return recursive_function()

try:
    recursive_function()
except RecursionError:
    print("Error: Maximum recursion depth exceeded")
```

---

### 10. Custom Exceptions
You can create your own exceptions for specific use cases.

**Example:**
```python
class CustomException(Exception):
    pass

try:
    raise CustomException("This is a custom error")
except CustomException as e:
    print(f"Caught a custom exception: {e}")
```

---

### 11. Handling Multiple Exceptions
You can catch multiple exceptions in a single block.

**Example:**
```python
try:
    x = int("abc")
    y = 1 / 0
except (ValueError, ZeroDivisionError) as e:
    print(f"Error occurred: {e}")
```

---

### 12. Using `finally` Block
The `finally` block executes no matter what happens.

**Example:**
```python
try:
    f = open("sample.txt", "r")
finally:
    print("Closing the file")
    f.close()
```

---
# Case Example: Student Grading System
A simple student grading system that includes handling of various potential exceptions like ValueError, KeyError, and ZeroDivisionError.

```python
def calculate_average(grades):
    try:
        if not grades:
            raise ValueError("No grades provided. Cannot calculate average.")
        total = sum(grades)
        average = total / len(grades)
        return average
    except ZeroDivisionError:
        print("Error: Division by zero occurred.")
        return None
    except TypeError:
        print("Error: Invalid type encountered in the grade list.")
        return None

def get_student_grade(students, name):
    try:
        return students[name]
    except KeyError:
        print(f"Error: Student '{name}' not found.")
        return None

# Example usage
students = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 95],
    "Charlie": []
}

try:
    # Accessing student data
    name = input("Enter student name: ")
    grades = get_student_grade(students, name)

    if grades is not None:
        # Calculate the average grade
        avg = calculate_average(grades)
        if avg is not None:
            print(f"Average grade for {name}: {avg:.2f}")
except Exception as e:
    print(f"Unexpected error: {e}")

print("Program executed successfully.")
```

These examples provide a comprehensive guide to understanding Python exceptions, their types, and how to handle them efficiently.
