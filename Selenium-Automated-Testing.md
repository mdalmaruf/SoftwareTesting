# Python Selenium Project

## What is Selenium?

Selenium is a popular open-source framework used to automate web browsers. It allows testers and developers to interact with web elements like buttons, forms, and links in a browser and perform automated actions (e.g., clicking, typing). It’s widely used for web application testing.

## Other Test Automation Tools

Here’s a broader list of tools used for **different types of automation testing**:

### **Web Testing Tools**
- **Cypress**: A JavaScript-based framework for end-to-end web testing.
- **Playwright**: Supports web automation across multiple browsers.
- **TestCafe**: JavaScript-based, easy to set up, no plugins required.

### **Mobile Testing Tools**
- **Appium**: Open-source tool for automating native and hybrid mobile apps.
- **Espresso**: Google’s framework for Android UI testing.
- **XCTest**: Apple's framework for iOS testing.

### **API Testing Tools**
- **Postman**: Popular for manual and automated API testing.
- **RestAssured**: A Java library for testing RESTful APIs.
- **SoapUI**: For functional testing of SOAP and REST APIs.

### **Desktop Testing Tools**
- **WinAppDriver**: Microsoft’s tool for automating Windows applications.
- **AutoIt**: For automating Windows desktop applications and GUI interactions.

### **Performance Testing Tools**
- **JMeter**: Open-source tool for performance and load testing.
- **Gatling**: Scala-based tool for load testing web applications.

---

## How Selenium Works and Why It’s Used

Selenium interacts with browsers through WebDriver, a tool that sends commands to a browser and retrieves results. It allows automation across multiple browsers and is used for:

- **Regression Testing**: Ensuring changes don’t break existing functionality.
- **Cross-Browser Testing**: Ensuring the app works across different browsers.
- **End-to-End Testing**: Verifying that entire workflows function as expected.

It is used primarily in web application testing, helping automate manual browser tasks.

---

## Explanation of How It Works

This project automates a web login process using **Selenium**, which allows Python code to interact with web elements just like a real user. Below is a step-by-step breakdown of how the program works:

1. **Install Dependencies**: We install Python libraries like Selenium, `pytest`, and `webdriver-manager`. Selenium controls the browser, and `pytest` helps us write and execute test cases.

2. **Setup WebDriver**: A WebDriver (like ChromeDriver) is configured using `webdriver-manager` to launch and control a browser (e.g., Chrome) automatically.

3. **Writing Test Cases**: Test cases are written using the `pytest` framework. The test interacts with the webpage by locating elements (like input fields and buttons) using Selenium's `find_element()` function.

4. **Automating Browser Actions**:
    - The browser navigates to a sample site (https://www.saucedemo.com/).
    - The program fills in a username and password and clicks the login button.
    - It checks if the login was successful by verifying the current URL.

5. **Parameterized Tests**: We use parameterization to test multiple login scenarios by passing different sets of usernames and passwords to a single test function.

6. **HTML Reports**: We can generate reports using `pytest-html`, providing a summary of test runs for better analysis.

7. **Running Tests**: Tests are executed from the command line using `pytest`. You can also specify the browser and generate HTML reports.

This automation setup can be expanded to include more complex workflows like form submissions, navigation between pages, or testing multiple browsers.

---

## Setting Up Selenium with Python

This guide will help you set up Selenium with Python for test automation.

### Installation

#### 1. Install Python and Virtual Environment

  - Install [Python](https://www.python.org/downloads/).
  - Ensure `pip` is installed by running:
  
  ```bash
  pip -V
  ```
  - Install virtual environment:
  ```bash
  python -m pip install virtualenv
  ```
  - Create and activate a virtual environment:
  ```bash
  python -m venv selenium-env
  selenium-env\Scripts\activate   # For Windows
  ```
#### 2. Set Up PyCharm (Optional)
  - Download `PyCharm`.
  - Create a new project and select the virtual environment created in the previous step as the interpreter.

#### 3. Install Requirements
  - Create a `requirements.txt` file with these contents:
  ```bash
  pytest==7.4.2
  selenium==4.13.0
  webdriver-manager==4.0.1
  ```
  - Install requirements:
  ```bash
  pip install -r requirements.txt
  ```
  #### 4. Create Basic Test
  - Create a test file called `test_login_page.py` in a `tests` folder.
  - Example test to automate logging into a sample website:
  ```python
  import time
  import pytest
  from selenium import webdriver
  from selenium.webdriver.common.by import By
  from selenium.webdriver.chrome.service import Service
  from webdriver_manager.chrome import ChromeDriverManager
  
  @pytest.fixture
  def driver():
      driver = webdriver.Chrome()
      driver.implicitly_wait(10)
      yield driver
      driver.quit()
  
  def test_valid_login(driver):
      driver.get("https://www.saucedemo.com/")
      time.sleep(2)
  
      username_input = driver.find_element(By.ID, "user-name")
      username_input.send_keys("standard_user")
  
      password_input = driver.find_element(By.ID, "password")
      password_input.send_keys("secret_sauce")
  
      login_btn = driver.find_element(By.ID, "login-button")
      login_btn.click()
  
      assert driver.current_url == "https://www.saucedemo.com/inventory.html"
  ```

##### Code Explanation
    - The `driver()` fixture initializes a Chrome browser using Selenium WebDriver.
    - implicitly_wait(10): Sets a timeout to wait for elements to load before throwing an error.
    - yield driver: Makes the WebDriver instance available to tests.
    - driver.quit(): Ensures the browser closes after each test to free up resources.
    - The `test_valid_login()` function tests valid login by entering correct credentials and validating the resulting URL.
    - Key Assertion: Ensures the user is redirected to the inventory page after logging in.



#### 5. Run Tests from Command Line
  - You can run the test using `pytest`:
  ```bash
  pytest tests/test_login_page.py
  ```

#### If You Encounter ChromeDriver Errors

If your Selenium tests fail due to ChromeDriver issues, try installing the driver manually.

##### **Manual WebDriver Download**  
[Download ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/#stable)

After downloading, extract the `chromedriver.exe` to a known location and update your code:

```python
@pytest.fixture
def driver():
    service = Service("C:/drivers/chromedriver.exe")  # Use full path
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
```


#### 6. Additional Test Example (Parameterized Test)
```python
#@pytest.mark.parametrize: Runs the same test with multiple inputs (different usernames and passwords).

@pytest.mark.parametrize("username, password, error", [
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("invalidUser", "invalidPass", "Epic sadface: Username and password do not match any user in this service")
])
def test_invalid_login(driver, username, password, error):
    driver.get("https://www.saucedemo.com/")
    
    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)

    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()

    error_msg_h3 = driver.find_element(By.TAG_NAME, "h3")
    assert error_msg_h3.text == error

```

#### 7. Run Tests with Parameters
```bash
pytest tests/test_login_page.py --browser=chrome
```

#### 8. Generate HTML Report
To create an HTML report, install the pytest-html library and run:
```bash
pip install pytest-html
pytest tests/test_login_page.py --html=reports/report.html
```

### Conclusion
This project sets up basic Selenium automation in Python, allowing you to automate browser actions like login flows, form filling, and more. You can expand it by adding more tests or integrating with CI/CD tools later.

  
