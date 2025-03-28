# Writing Unit Tests and Checking Code Coverage in Python

## Introduction
In this blog, we will demonstrate how to write unit tests for a Python program and measure the code coverage. Code coverage is an essential metric that helps in assessing how much of your code is tested by your test suite. We will go through the steps to set this up in both **PyCharm** and **VS Code**, including how to run the tests and check coverage.
Check the link for PyCharm: https://www.jetbrains.com/help/pycharm/running-test-with-coverage.html

## What is Code Coverage?
**Code Coverage** is a measure used to describe the degree to which the source code of a program is tested by running tests. It helps to identify untested parts of the code. High code coverage indicates that the majority of your code has been executed during testing, which can reduce the likelihood of bugs in untested code paths.

### Steps Covered in This Tutorial:
1. Write a simple program
2. Create unit tests for that program
3. Measure code coverage
4. Add more tests to improve coverage

---

## 1. Writing a Simple Program

Let's create a simple program called `math_operations.py` that performs basic arithmetic operations.

```python
# math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```
## 2. Writing Unit Tests

Next, we create a test file `test_math_operations.py` to write unit tests for this program using the `unittest` module.
```python
# test_math_operations.py

import unittest
from math_operations import add, subtract, multiply, divide

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 0), 0)

if __name__ == '__main__':
    unittest.main()

```

### Running the Tests:

- PyCharm: Right-click on the `test_math_operations.py` file and select Run 'Unittest'.

- VS Code: In the terminal, run:

```bash
python -m unittest test_math_operations.py

```
## 3. Measuring Code Coverage
Now, let's measure the code coverage for the unit tests. For this, we'll use the coverage.py library.

- ### Installing `coverage.py`:
  - Run the following command to install coverage in your terminal:
```bash
  pip install coverage
```
  
- ### Checking Code Coverage:
  - To measure the coverage, first run the tests with coverage tracking:
 
  ```bash
    coverage run -m unittest discover 
  ```
  or 
  ```bash
     coverage run -m unittest test_math_operations.py
   ```
  - ### After running the tests, generate the coverage report:
```bash
python -m coverage report
```
or
```bash
coverage report
```

This will show how much of your code has been executed during testing.

## 4. Improving Code Coverage
As it stands, we have not written tests for the multiply and divide functions. Let's add them now to improve the code coverage.

### Adding More Tests:
```python
# test_math_operations.py

import unittest
from math_operations import add, subtract, multiply, divide

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
```

### Running the Tests Again:
After adding the new tests, you can run the tests again and check the updated coverage.

  - PyCharm: As before, right-click on the test file and run Unittest.

  - VS Code: In the terminal, run:

```bash
python -m unittest test_math_operations.py
```

### Rechecking Code Coverage:

```bash
coverage run -m unittest test_math_operations.py
```
or 
```bash
python -m coverage report
```
```bash
coverage report

```
Generate the updated coverage report in html:

```bash
coverage html

```
## Additional Example of UnitTest for finding Minium Value
```python
# minimum.py
def find_minimum(elements):
    if not elements:
        raise ValueError("The list is empty")

    try:
        elements = [int(el) for el in elements]  # Try converting all elements to integers
    except (ValueError, TypeError):
        raise ValueError("List contains non-integer values")

    return min(elements)
```


```python
# test_minimum.py

import unittest
from main import find_minimum

class TestMinimumFunction(unittest.TestCase):

    def test_case_1(self):
        # Test Case 1: Very short list with 1, 2, or 3 elements (This will pass)
       self.assertEqual(find_minimum([90]), 90)  # Single element
       self.assertEqual(find_minimum([12, 10]), 10)  # Two elements
       self.assertEqual(find_minimum([36, 14, 12]), 12)  # Three elements

    def test_case_2(self):
        # Test Case 2: Empty list
        with self.assertRaises(ValueError):
            find_minimum([])

    def test_case_3(self):
        # Test Case 3: Minimum element is the first or last
        self.assertEqual(find_minimum([10, 23, 34, 81, 97]), 10)
        self.assertEqual(find_minimum([97, 81, 34, 23, 10]), 10)

    def test_case_4(self):
        # Test Case 4: List with negative elements
        self.assertEqual(find_minimum([10, -2, 5, 23]), -2)
        self.assertEqual(find_minimum([10, -2, -24, 4]), -24)

    def test_case_5(self):
        # Test Case 5: All elements are negative
        self.assertEqual(find_minimum([-23, -31, -45, -56]), -56)
        self.assertEqual(find_minimum([-6, -203, -2, -78]), -203)

    def test_case_6(self):
        # Test Case 6: List with some real numbers
        with self.assertRaises(ValueError):
            find_minimum([23, '*', 67, 33])

    def test_case_7(self):
        # Test Case 7: List with alphabetic and special characters
        with self.assertRaises(ValueError):
            find_minimum([23, "hi", 32, 1])
        with self.assertRaises(ValueError):
            find_minimum([12, "&", "*", "34m", "!"])

    def test_case_8(self):
        # Test Case 8: List with duplicate elements
        self.assertEqual(find_minimum([3, 4, 6, 9, 6]), 3)
        self.assertEqual(find_minimum([13, 6, 6, 9, 15]), 6)

    def test_case_9(self):
        # Test Case 9: List with one large number
        self.assertEqual(find_minimum([530, 42444672, 97, 23, 46, 59]), 23)


if __name__ == "__main__":
    unittest.main()


```


