# Lab 3: Unit Testing - INFT 1207

## Project Overview
This project involves calculating the areas of four shapes:
- **Circle**
- **Trapezium**
- **Ellipse**
- **Rhombus**

Additionally, it contains a **menu-driven test suite** to allow users to select the shape they want to test. The goal is to fix the provided code, add support for new shapes, and implement unit tests using Python’s `unittest` framework.

---

## Instructions and Steps

### 1. Set Up the Project in PyCharm
1. Open **PyCharm** and create a new **Python Project**. Name it `Lab3_GroupN` (replace `N` with your group number).
2. Inside the project folder, create two subdirectories:
   - `app` (to store the application code)
   - `test` (to store the test code)
3. Create the following files:
   - In the **app** folder: `Lab3_firstname1_firstname2.py`
   - In the **test** folder: `test_Lab3_firstname1_firstname2.py`
   - At the project root: `test_suite.py`

---

### 2. Application Code (Lab3_firstname1_firstname2.py)
Place the following code in **`app/Lab3_firstname1_firstname2.py`**:

```python
from math import pi

def circle_area(r):
    if isinstance(r, (int, float)) and r >= 0:
        return pi * (r ** 2)
    else:
        raise ValueError("Invalid radius. Must be a non-negative number.")

def trapezium_area(a, b, h):
    return 0.5 * (a + b) * h
    

def ellipse_area(a, b):
    return pi * a * b
  

def rhombus_area(d1, d2):
    return 0.5 * d1 * d2
    
```

---

### 3. Unit Test Code (test_Lab3_firstname1_firstname2.py)
Place the following code in **`test/test_Lab3_firstname1_firstname2.py`**:

```python
import unittest
from app.Lab3_firstname1_firstname2 import circle_area, trapezium_area, ellipse_area, rhombus_area

class TestShapes(unittest.TestCase):

    def setUp(self):
        print("Setup: Preparing tests...")

    def tearDown(self):
        print("Teardown: Cleaning up after tests...")

    def test_circle_area_valid(self):
        self.assertAlmostEqual(circle_area(3), 28.274333882308138)

    def test_circle_area_invalid(self):
        with self.assertRaises(ValueError):
            circle_area(-1)

   //def test_trapezium_area_valid(self):
        

    //def test_trapezium_area_invalid(self):
       

    //def test_ellipse_area_valid(self):
        

    //def test_ellipse_area_invalid(self):
      

    //def test_rhombus_area_valid(self):
     
    //def test_rhombus_area_invalid(self):
        
if __name__ == "__main__":
    unittest.main()
```

---

### 4. Menu-Driven Test Suite (test_suite.py)
Add the following code to **`test_suite.py`**:

```python
import unittest

def run_tests(choice):
    if choice == 'c':
        suite = unittest.defaultTestLoader.loadTestsFromName('test.test_Lab3_firstname1_firstname2.TestShapes.test_circle_area_valid')
    elif choice == 't':
        suite = unittest.defaultTestLoader.loadTestsFromName('test.test_Lab3_firstname1_firstname2.TestShapes.test_trapezium_area_valid')
    elif choice == 'e':
        suite = unittest.defaultTestLoader.loadTestsFromName('test.test_Lab3_firstname1_firstname2.TestShapes.test_ellipse_area_valid')
    elif choice == 'r':
        suite = unittest.defaultTestLoader.loadTestsFromName('test.test_Lab3_firstname1_firstname2.TestShapes.test_rhombus_area_valid')
    else:
        print("Invalid choice. Exiting.")
        return

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    print("Enter a shape to test ('c' for Circle, 't' for Trapezium, 'e' for Ellipse, 'r' for Rhombus):")
    choice = input().strip().lower()
    run_tests(choice)
```

---

### 5. Project Structure
```
Lab3_GroupN/
│
├── app/
│   └── Lab3_firstname1_firstname2.py  # Application code for area calculations
│
├── test/
│   └── test_Lab3_firstname1_firstname2.py  # Unit tests for shapes
│
├── test_suite.py  # Menu-driven test suite
│
└── README.md  # Project instructions
```

---

### 6. How to Run the Project


1. **Run the application**:
   ```bash
   python app/Lab3_firstname1_firstname2.py
   ```

2. **Run the tests**:
   ```bash
   python test/test_Lab3_firstname1_firstname2.py
   ```

3. **Run the menu-driven test suite**:
   ```bash
   python test_suite.py
   ```

---

### 7. Test Case Documentation
Create a **test case design document** that includes:
- **Test case ID**
- **Description**
- **Input values**
- **Expected output**
- **Actual output**
- **Pass/Fail status**

---

### 8. Submission Guidelines

1. **Files of the project folder** containing:
   - Application code + Test code + Test suite
   - Test case document + Screenshots of your Test Case Running
   - GitHub Link: Create a GitHub Project and Submit the project over there with a Readme.md file


2. **Submit a video** where each partner explains:
   - Code implementation
   - Test design and results
   - Task distribution

---

### 9. Team Members
- **Student 1**: Firstname1 Lastname1
- **Student 2**: Firstname2 Lastname2

---
---
---
# Helpful Resources for Unit Testing

This document outlines unit testing strategies for four geometric shapes: **Circle, Trapezium, Ellipse, and Rhombus**.

## 1. Circle
A circle is defined by its **radius (r)**. Important properties include **area and circumference**.

### Key Formulas:
- **Area:** \( A = \pi r^2 \)
- **Circumference:** \( C = 2\pi r \)
- **Diameter:** \( D = 2r \)

### Possible Unit Tests:
- ✅ Verify **area** calculation for various radii.
- ✅ Verify **circumference** calculation.
- ✅ Check if **diameter** is correctly computed as \( 2r \).
- ✅ Test **edge cases**:
  - **r = 0** → Area & circumference should be 0.
  - **r = 1** → Expected values \( \pi \) for area and \( 2\pi \) for circumference.
  - **Negative radius** → Should raise an exception.
- ✅ **Floating-point precision** checks.

---

## 2. Trapezium (Trapezoid)
A **trapezium** is a quadrilateral with at least one pair of **parallel sides**.

### Key Formulas:
- **Area:** \( A = \frac{1}{2} (a + b) h \)  
  where \( a \) and \( b \) are the **parallel sides**, and \( h \) is the **height**.
- **Perimeter:** \( P = a + b + c + d \), where \( a, b, c, d \) are the four sides.

### Possible Unit Tests:
- ✅ Verify **area** and **perimeter** calculations.
- ✅ Test **edge cases**:
  - **h = 0** → Area should be 0.
  - **Negative side lengths** → Should raise an error.
  - **All sides equal** → Should behave as a parallelogram.
- ✅ **Floating-point precision** checks.

---

## 3. Ellipse
An **ellipse** is defined by its **semi-major axis (a)** and **semi-minor axis (b)**.

### Key Formulas:
- **Area:** \( A = \pi a b \)
- **Perimeter (Approximate):**
  \( P \approx \pi [3(a + b) - \sqrt{(3a + b)(a + 3b)}] \)

### Possible Unit Tests:
- ✅ Verify **area** and **perimeter** calculations.
- ✅ Test **edge cases**:
  - **a = b** → Should behave like a circle.
  - **a or b = 0** → Area should be 0.
  - **Negative values** → Should raise an error.
- ✅ **Floating-point precision** checks.

---

## 4. Rhombus
A **rhombus** is a **parallelogram** with all **four sides equal**.

### Key Formulas:
- **Area:** \( A = \frac{1}{2} d_1 d_2 \)  
  where \( d_1 \) and \( d_2 \) are the diagonals.
- **Perimeter:** \( P = 4s \), where \( s \) is the side length.

### Possible Unit Tests:
- ✅ Verify **area** and **perimeter** calculations.
- ✅ Test **edge cases**:
  - **Diagonal lengths = 0** → Area should be 0.
  - **Side length = 0** → Perimeter should be 0.
  - **Diagonal lengths forming a square** → Special case validation.
- ✅ **Floating-point precision** checks.

---

## General Unit Testing Approach
- Use **assertions** to compare expected vs. actual values.
- Implement **parameterized tests** to check multiple inputs at once.
- Test **invalid inputs** (negative values, zero where inappropriate).
- Use **edge cases** to ensure robust handling of extreme inputs.


