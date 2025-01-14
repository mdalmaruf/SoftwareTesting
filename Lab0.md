
# Lab0: Basic Software Testing in Python

## Objective
This lab introduces the concepts of **Unit Testing** and **Integration Testing** in Python using PyCharm. We will also cover basic Git and GitHub operations, such as forking, pushing, and pulling a project.

---

## Prerequisites
Before starting, ensure you have the following installed:
1. **Python 3.10+**
2. **PyCharm IDE**
3. **Git**

---

## Step 1: Setting Up Git and GitHub
### Install Git
1. Download Git from the [official website](https://git-scm.com/).
2. Follow the installation instructions for your operating system.
3. Verify installation by running:
   ```bash
   git --version
   ```

### Set Up GitHub
Please follow this [YouTube Video Link](https://www.youtube.com/watch?v=sVuV9Z0vM5g) for more details.
1. Create a GitHub account at [github.com](https://github.com).
2. Configure Git with your username and email:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your-email@example.com"
   ```

### Fork the Project
1. Visit the GitHub repository: [Example Repo](https://github.com/example/testing-lab).
2. Click **Fork** to copy the repository to your GitHub account.

### Clone the Repository Locally
1. Copy the repository URL from your forked repository.
2. Clone it using Git:
   ```bash
   git clone https://github.com/your-username/testing-lab.git
   ```

### Try Push and Pull Operations
1. Make changes to the code locally (you’ll do this later in the lab).
2. Push changes to your forked repository:
   ```bash
   git add .
   git commit -m "Initial test changes"
   git push origin main
   ```
3. Pull changes from the original repository (if any):
   ```bash
   git pull upstream main
   ```

---

## Step 2: Create a PyCharm Project for Testing
1. Open PyCharm and create a new project or open the cloned repository.
2. Ensure Python is configured as the project interpreter.

---

## Step 3: Write Unit Tests
Unit tests validate individual functions or methods in isolation.

### Example: Calculator Program
**calculator.py**
```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

**test_calculator.py**
```python
# test_calculator.py
import unittest
from calculator import add, subtract

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)
    
    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 1), -1)

if __name__ == "__main__":
    unittest.main()
```

### Run Unit Tests
1. Right-click on `test_calculator.py` in PyCharm.
2. Select **Run 'Unittest in test_calculator'**.

---

## Step 4: Write Integration Tests
Integration tests validate the interaction between multiple components.

**calculator_app.py**
```python
# calculator_app.py
from calculator import add, subtract

def calculate(operation, a, b):
    if operation == "add":
        return add(a, b)
    elif operation == "subtract":
        return subtract(a, b)
    else:
        raise ValueError("Invalid operation")
```

**test_calculator_app.py**
```python
# test_calculator_app.py
import unittest
from calculator_app import calculate

class TestCalculatorApp(unittest.TestCase):
    def test_calculate_add(self):
        self.assertEqual(calculate("add", 2, 3), 5)
    
    def test_calculate_subtract(self):
        self.assertEqual(calculate("subtract", 5, 2), 3)
    
    def test_calculate_invalid(self):
        with self.assertRaises(ValueError):
            calculate("multiply", 2, 3)

if __name__ == "__main__":
    unittest.main()
```

### Run Integration Tests
1. Right-click on `test_calculator_app.py` in PyCharm.
2. Select **Run 'Unittest in test_calculator_app'**.

---

## Step 5: Push Code to GitHub
1. Add changes to Git:
   ```bash
   git add .
   git commit -m "Added unit and integration tests"
   git push origin main
   ```

2. Verify changes in your GitHub repository.

---

## Summary
- You’ve learned the difference between **Unit Testing** and **Integration Testing**.
- You’ve set up Git and GitHub to manage your project effectively.
- **Next Steps**:
  - Experiment with more complex functions.
  - Explore tools like `pytest` for testing.

---

Download the example files and scripts from the GitHub repository: [Example Repo](https://github.com/example/testing-lab).
