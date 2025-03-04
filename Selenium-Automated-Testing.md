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
## **Selenium Tool Suite - Differences and Real-World Examples**

The Selenium Tool Suite consists of different components used for test automation. Below is a breakdown of each component, its functionality, and real-world applications.

### **Selenium IDE**
**Definition:**
Selenium IDE (Integrated Development Environment) is a **record-and-playback tool** that allows users to create test cases without writing any code.

🔹 **Real-World Example:**
Imagine you want to **automate filling out a contact form** on a website but don’t know programming.
- With Selenium IDE, you **record** your actions (typing, clicking buttons, etc.).
- Then, you **replay the recorded test** to verify if the form works as expected.

**🟢 Best For:**
- Beginners with no coding experience.
- Quick prototype automation.

**🔴 Limitations:**
- Cannot handle complex logic.
- Limited support for parallel execution.

---

### **Selenium Remote Control (RC) (Deprecated)**
**Definition:**
Selenium RC was an **older version of Selenium** that allowed automation by injecting JavaScript into the browser.

🔹 **Real-World Example:**
Assume you're testing an **e-commerce site** and need to verify checkout across different browsers.
- Selenium RC allows you to **run tests remotely** across multiple browsers.
- But it is **slower** because it requires a separate **Selenium Server** to interact with the browser.

**🟢 Best For:**
- Cross-browser testing (before WebDriver was introduced).

**🔴 Limitations:**
- Requires a running Selenium server.
- Slower due to JavaScript injection.
- Now **deprecated** in favor of WebDriver.

---

### **Selenium WebDriver (Current Standard)**
**Definition:**
Selenium WebDriver is a modern **browser automation framework** that directly interacts with the browser **without requiring a separate server**.

🔹 **Real-World Example:**
If you want to **automate login to a banking portal**, WebDriver can:
- Open the browser.
- Enter login credentials.
- Click the login button.
- Verify that the user is redirected to the account dashboard.

**🟢 Best For:**
- Modern web automation.
- Handling dynamic web elements.
- Fast execution.

**🔴 Limitations:**
- Cannot handle parallel execution alone (needs Selenium Grid).
- Requires programming knowledge.

---

### **Selenium Grid**
**Definition:**
Selenium Grid allows running tests **on multiple machines, browsers, and operating systems in parallel**.

🔹 **Real-World Example:**
A **travel booking website** needs to test its search functionality on:
- Chrome (Windows)
- Firefox (Mac)
- Edge (Linux)

Instead of running tests **one by one**, Selenium Grid distributes the test cases across different **nodes** (machines), **saving execution time**.

**🟢 Best For:**
- Parallel execution.
- Large-scale automation projects.

**🔴 Limitations:**
- Requires proper setup and configuration.
- Increased infrastructure complexity.

---

## **3. Evolution of Selenium (Selenium 1, 2, and 3)**

### **Selenium 1 (RC) vs Selenium 2 (WebDriver)**
| Feature | Selenium RC (Old) | Selenium WebDriver (Modern) |
|---------|----------------|------------------|
| Server Requirement | Needs Selenium Server | Direct browser interaction |
| Speed | Slower | Faster |
| API Simplicity | Complex | Easy |
| Parallel Execution | Not efficient | Supported with Selenium Grid |

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
    service = Service("C:/chromedriver-win64/chromedriver.exe")  # Use full path 
    driver = webdriver.Chrome(service=service)
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
    service = Service("C:/chromedriver-win64/chromedriver.exe")  # Use full path 
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






## **How Selenium Works - Step by Step**

Selenium automates browsers by interacting with them at a lower level using WebDriver, which acts as a bridge between the Selenium code and the browser. Let's break it down step by step.

### **Step 1: Selenium Code Execution**
When we run a Selenium script in Python (or any other language), the Selenium WebDriver API sends a request to the browser-specific WebDriver (e.g., ChromeDriver, GeckoDriver).

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")
```

#### **What Happens Here?**
- The **Selenium script** (Python code) initializes a browser instance.
- The **WebDriver (e.g., ChromeDriver)** acts as an intermediary between the script and the actual browser.
- A **request is sent from the Selenium WebDriver to the browser** via a WebSocket communication protocol.
- The **browser receives the request** and processes it.
- The **browser executes the requested action**, such as opening a URL or interacting with elements.
- The **response is sent back** to the WebDriver, which then relays the result to Selenium.

### **Step 2: Communication Between Selenium and the Browser**
Selenium communicates with the browser through a **JSON Wire Protocol**. This is a RESTful API that sends HTTP requests from Selenium WebDriver to the browser.

- Selenium sends a **HTTP request** containing instructions (e.g., open URL, click button).
- The WebDriver forwards this request to the actual browser.
- The browser **processes the request** and performs the required action.
- The browser then **returns an HTTP response** with a status code (success, failure, etc.).
- Selenium receives the response and executes the next command in the script.

### **Step 3: How Requests Are Processed**
For example, when running:
```python
driver.get("https://www.google.com")
```
- **Selenium WebDriver** sends an HTTP `POST` request to the WebDriver server (e.g., ChromeDriver) with the command to navigate to the URL.
- **The WebDriver server** forwards the command to the browser.
- **The browser** processes the request and loads the page.
- **A response** is sent back confirming the page has loaded.

### **Step 4: Element Interaction**
When finding and interacting with elements:
```python
element = driver.find_element(By.NAME, "q")
element.send_keys("Selenium WebDriver")
```
- **Selenium WebDriver** sends a `FIND ELEMENT` HTTP request to ChromeDriver.
- **ChromeDriver** executes JavaScript in the browser to locate the element.
- **A response** is sent back to WebDriver with the element details.
- **WebDriver sends another request** to simulate typing into the element.

### **Step 5: Receiving Responses**
Selenium receives responses in JSON format:
```json
{
    "sessionId": "123456",
    "status": 0,
    "value": "Page loaded successfully"
}
```
A `status: 0` means success, while an error code means failure.

---







  
