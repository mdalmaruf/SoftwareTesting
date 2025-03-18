# ICE 5: Selenium Locating Strategies

This assignment involves creating a Selenium test automation script in Python to register and log in a user on the Guru99 demo site. Follow these step-by-step instructions to set up and run the project in PyCharm.

## Project Setup

### Step 1: Create Project and Virtual Environment
1. Open **PyCharm** and create a new project named `ICE5`.
 ```bash
   pip install selenium pytest webdriver-manager
   ```
  

## Step 2: Create Test Folder and Test File
1. Inside the project folder `ICE5`, create a new folder called `test`.
2. Within the `test` folder, create a Python file named `test_cases.py`.

## Code Implementation

### Step 3: Define Test Cases in `test_cases.py`

#### Register User Test Case:
- Navigate to the registration page at [Guru99 Registration](http://demo.guru99.com/test/newtours/).
- Locate and fill in each input field (e.g., First Name, Last Name, Phone, etc.) using Selenium locators such as ID, Name, XPath, or CSS Selectors.
- Submit the form to create a new user with your first name and password.

#### Login and Assertion Test Case:
- Log in to the site using the credentials created in the registration step.
- Use assertions to verify that the login is successful.

### Example Code Structure for `test_cases.py`

Organize your code into functions for readability and maintainability:

```python

# Importing libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class Guru99Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Or specify the WebDriver path

    def test_register_user(self):
        driver = self.driver
        driver.get("http://demo.guru99.com/test/newtours/register.php")

        # Add registration steps here using locators
        # Example: driver.find_element(By.NAME, "firstName").send_keys("YourFirstName")
        # Add assertion to confirm registration success (customize as needed)

    def test_login_user(self):
        driver = self.driver
        driver.get("http://demo.guru99.com/test/newtours/")

        # Add login steps here and assert successful login
        # Example: driver.find_element(By.NAME, "userName").send_keys("YourFirstName")
        # Add assertion to verify login success (customize as needed)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
```


**Screenshots**: Take screenshots of the running test cases to include in your submission.



Sample:
```python

# Importing libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # Add this line for Select

import unittest

class Guru99Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Or specify the WebDriver path

    def test_register_user(self):
        driver = self.driver
        driver.get("http://demo.guru99.com/test/newtours/register.php")

        # Filling out Contact Information fields
        driver.find_element(By.NAME, "firstName").send_keys("John")
        driver.find_element(By.NAME, "lastName").send_keys("Doe")
        driver.find_element(By.NAME, "phone").send_keys("1234567890")
        driver.find_element(By.NAME, "userName").send_keys("johndoe@example.com")

        # Filling out Mailing Information fields
        driver.find_element(By.NAME, "address1").send_keys("123 Elm Street")
        driver.find_element(By.NAME, "city").send_keys("Metropolis")
        driver.find_element(By.NAME, "state").send_keys("Central State")
        driver.find_element(By.NAME, "postalCode").send_keys("54321")

        # Selecting a country from the dropdown
        country_dropdown = Select(driver.find_element(By.NAME, "country"))
        country_dropdown.select_by_visible_text("UNITED STATES")

        # Filling out User Information fields
        driver.find_element(By.NAME, "email").send_keys("JohnDoe")
        driver.find_element(By.NAME, "password").send_keys("mySecurePassword123")
        driver.find_element(By.NAME, "confirmPassword").send_keys("mySecurePassword123")

        # Submit the registration form
        driver.find_element(By.NAME, "submit").click()

        # Using XPath to locate the success message and verify registration success
        success_message = driver.find_element(By.XPATH, "//font[contains(text(),'Thank you for registering.')]")
        self.assertIsNotNone(success_message)

        # Here, check for a successful registration message or redirection (customize as needed)
        # self.assertIn("Thank you for registering", driver.page_source)


        # Add registration steps here using locators
        # Example: driver.find_element(By.NAME, "firstName").send_keys("YourFirstName")
        # Add assertion to confirm registration success (customize as needed)

    # def test_login_user(self):
    #     driver = self.driver
    #     driver.get("http://demo.guru99.com/test/newtours/")

        # Add login steps here and assert successful login
        # Example: driver.find_element(By.NAME, "userName").send_keys("YourFirstName")
        # Add assertion to verify login success (customize as needed)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
```

