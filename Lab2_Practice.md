# Week-5-Lab: Running Unit Tests with Assert Methods in PyCharm

## Step 1: Set up the Project in PyCharm

1. **Open PyCharm** on your machine.
2. **Create a New Project**:
   - Go to the **File** menu, click on **New Project**.
   - Name the project as `Week-5-Lab` and choose a location to save the project.
   - Ensure that the correct Python interpreter is selected for the project.
3. **Create Two Python Files**:
   - **Right-click** on the project folder `Week-5-Lab` in the Project Explorer.
   - Select **New > Python File** and name it `program.py` to store the main functions.
   - Create another file, **New > Python File**, and name it `test_program.py` to store the unit tests.

## Step 2: Write the Program Code

1. **Open `program.py`** and add the following code:

```python
# program.py

def add(x, y):
    return x + y

def is_even(num):
    return num % 2 == 0

def get_user():
    return None

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
```
## Step 3: Write the Unit Test Code
1. Open `test_program.py` and add the following code to write test cases using assert methods:

```python
# test_program.py

import unittest
from program import add, is_even, get_user, divide

class TestSimpleFunctions(unittest.TestCase):

    # 1. assertEqual: Checks if two values are equal
    def test_add(self):
        self.assertEqual(add(5, 5), 10)

    # 2. assertTrue: Checks if a value evaluates to True
    def test_is_even(self):
        self.assertTrue(is_even(4))

    # 3. assertFalse: Checks if a value evaluates to False
    def test_is_not_even(self):
        self.assertFalse(is_even(5))

    # 4. assertIs: Checks if two variables refer to the same object
    def test_same_object(self):
        result = add(2, 3)
        expected_result = 5
        self.assertIs(result, expected_result)

    # 5. assertIsNone: Checks if a value is None
    def test_is_none(self):
        self.assertIsNone(get_user())

    # 6. assertIsNotNone: Checks if a value is not None
    def test_is_not_none(self):
        user = "Alice"
        self.assertIsNotNone(user)

    # 7. assertIn: Checks if a value is in a container (e.g., list)
    def test_item_in_list(self):
        my_list = [1, 2, 3, 4, 5]
        self.assertIn(3, my_list)

    # 8. assertNotIn: Checks if a value is not in a container
    def test_item_not_in_list(self):
        my_list = [1, 2, 3, 4, 5]
        self.assertNotIn(6, my_list)

    # 9. assertRaises: Checks if a specific exception is raised
    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 10, 0)

    # 10. assertAlmostEqual: Checks if two values are approximately equal (useful for floating-point numbers)
    def test_approximate_equal(self):
        result = divide(10, 3)
        self.assertAlmostEqual(result, 3.33, places=2)

if __name__ == '__main__':
    unittest.main()
```

## Step 4: Explanation of Assertion Methods

- **assertEqual(a, b)**: Checks if `a` and `b` are equal.
  - Example: `self.assertEqual(add(5, 5), 10)` checks if `add(5, 5)` returns `10`.

- **assertTrue(x)**: Checks if `x` is `True`.
  - Example: `self.assertTrue(is_even(4))` passes if `is_even(4)` is `True`.

- **assertFalse(x)**: Checks if `x` is `False`.
  - Example: `self.assertFalse(is_even(5))` passes if `is_even(5)` is `False`.

- **assertIs(a, b)**: Checks if `a` and `b` are the same object.
  - Example: `self.assertIs(result, expected_result)` passes if `result` and `expected_result` are the same object.

- **assertIsNone(x)**: Checks if `x` is `None`.
  - Example: `self.assertIsNone(get_user())` passes if `get_user()` returns `None`.

- **assertIsNotNone(x)**: Checks if `x` is not `None`.
  - Example: `self.assertIsNotNone(user)` passes if `user` is not `None`.

- **assertIn(a, b)**: Checks if `a` is present in `b`.
  - Example: `self.assertIn(3, my_list)` passes if `3` is in `my_list`.

- **assertNotIn(a, b)**: Checks if `a` is not present in `b`.
  - Example: `self.assertNotIn(6, my_list)` passes if `6` is not in `my_list`.

- **assertRaises(exception, callable, *args)**: Checks if calling `callable` raises the `exception`.
  - Example: `self.assertRaises(ValueError, divide, 10, 0)` passes if `divide(10, 0)` raises a `ValueError`.

- **assertAlmostEqual(a, b, places)**: Checks if `a` and `b` are approximately equal up to `places` decimal places.
  - Example: `self.assertAlmostEqual(result, 3.33, places=2)` passes if `result` is approximately equal to `3.33` up to 2 decimal places.

### Step 5: Run the Tests in PyCharm

1. In PyCharm, **right-click** on the `test_program.py` file.
2. Click on **Run 'test_program'**.

### Expected Output:
If all tests pass, you will see a message like this:

```bash
..........
----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK
```
