# Setting Up Virtual Environment in Python, Running a Program, and Writing a Test Case

## Step 1: Install and Set Up Virtual Environment
1. Open a terminal and navigate to your project directory:
   ```bash
   cd your_project_directory
   ```
2. Create a virtual environment using the following command:
 ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows:
     ```bash
        venv\Scripts\activate
     ```
   - Mac/Linux:
     ```bash
        source venv/bin/activate
     ```
Confirm the virtual environment is activated: The terminal prompt should show (venv) at the beginning.


## Step 2: Install a Library and Run a Program

### Install the `requests` library:
```bash
pip install requests
```

### Create a folder structure:
```plaintext
my_project/
├── src/
│   └── main.py
├── tests/
│   └── test_main.py
├── venv/
```

### Write a simple program in `src/main.py`:
```python
import requests

def fetch_data(url):
    """Fetch data from the given URL."""
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts/1"
    data = fetch_data(url)
    print("Fetched Data:")
    print(data)
```

### Run the program:
```bash
python src/main.py
```

The program will fetch and display data from the given URL.

---

## Step 3: Write a Test Case

### Write a test case in `tests/test_main.py`:
```python
import unittest
from src.main import fetch_data

class TestFetchData(unittest.TestCase):
    def test_fetch_data(self):
        """Test the fetch_data function with a mock URL."""
        url = "https://jsonplaceholder.typicode.com/posts/1"
        result = fetch_data(url)
        self.assertIn("userId", result)  # Check if the response contains the key "userId"

if __name__ == "__main__":
    unittest.main()
```

### Run the test:
```bash
python -m unittest tests/test_main.py
```

The test will pass if the `fetch_data` function works correctly.

---

## Summary

- **Virtual Environment**: Isolate dependencies using `python -m venv venv`.
- **Activate Environment**: Use `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux).
- **Install Libraries**: Install libraries using `pip install <library>`.
- **Run Program**: Execute Python scripts using `python <file_path>`.
- **Write Tests**: Use `unittest` to validate your code with test cases.

## Lab0 : factorial.py

```python

def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
   
    number = int(input("Enter a number: "))
    print(f"Factorial of {number} is {factorial(number)}.")
```   

## test_factorial.py

```python
import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

if __name__ == "__main__":
    unittest.main()
```



