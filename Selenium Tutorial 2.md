# **Python Selenium Automation Guide**

## **1. Introduction to Selenium**

Selenium is a popular open-source framework used to automate web browsers. It allows testers and developers to interact with web elements like buttons, forms, and links in a browser and perform automated actions (e.g., clicking, typing). It’s widely used for web application testing.

### **Why Use Selenium?**

- **Cross-browser testing** – Works with Chrome, Firefox, Edge, and Safari.
- **Automates repetitive tasks** – Form filling, button clicks, and navigation.
- **Supports multiple programming languages** – Python, Java, C#, etc.
- **Compatible with various testing frameworks** – PyTest, UnitTest, etc.

## **2. Other Test Automation Tools**

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

### **Performance Testing Tools**

- **JMeter**: Open-source tool for performance and load testing.
- **Gatling**: Scala-based tool for load testing web applications.

---

## **3. How Selenium Works**

Selenium interacts with browsers through WebDriver, a tool that sends commands to a browser and retrieves results. It allows automation across multiple browsers and is used for:

- **Regression Testing**: Ensuring changes don’t break existing functionality.
- **Cross-Browser Testing**: Ensuring the app works across different browsers.
- **End-to-End Testing**: Verifying that entire workflows function as expected.

---

## **4. Setting Up Selenium in Python**

### **Step 1: Install Selenium**

```bash
pip install selenium
```

### **Step 2: Download and Setup WebDriver**

Each browser requires a WebDriver to communicate with Selenium. Download the appropriate WebDriver:

- **Chrome**: [https://googlechromelabs.github.io/chrome-for-testing/#stable](https://googlechromelabs.github.io/chrome-for-testing/#stable)
- **Firefox (GeckoDriver)**: [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)

#### **Where to Place the WebDriver?**

After downloading, **place the WebDriver in a system path directory** or specify the full path in your script. If not set correctly, Selenium will throw a `WebDriverException` stating that the driver cannot be found.

```python
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#service = Service(ChromeDriverManager().install())
service = Service("C:/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")
time.sleep(3)
```

If the WebDriver is not in the correct location, Selenium will raise an error like:

```bash
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH.
```

To fix this, ensure the WebDriver is in the correct directory or explicitly provide the path:

```python
service = Service("C:/path/to/chromedriver.exe")
driver = webdriver.Chrome(service=service)
```

---

## **5. Complete Selenium WebDriver & SearchContext Method Cheat Sheet**

### **1. Browser Navigation Methods**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open a website
driver.get("https://www.example.com")
time.sleep(2)  # Wait for page to load

# Find an element by ID and extract text
element = driver.find_element(By.TAG_NAME, "h1")
print("Page heading:", element.text)

# Print the title, source code, and current URL
print("Page Title:", driver.title)
print("Page Source (truncated):", driver.page_source[:500])  # Print first 500 characters
print("Current URL:", driver.current_url)

# Close the browser
driver.quit()
```

### **2. Navigating Between Pages**

```python
driver.back()  # Navigate back
driver.forward()  # Navigate forward
driver.refresh()  # Refresh page
```

### **3. Element Interaction Methods**

```python
from selenium.webdriver.common.by import By

element = driver.find_element(By.ID, "submitButton")
element.click()  # Click an element
```

#### **What is **``**?**

```python
element.send_keys("text")  # Enter text in an input field
```

`send_keys()` is used to simulate keyboard input. It allows you to enter text into input fields, search bars, or text areas.

```python
element.clear()  # Clear text field
element.is_displayed()  # Check if element is visible
element.is_enabled()  # Check if element is enabled
element.is_selected()  # Check if checkbox/radio button is selected
element.get_attribute("value")  # Get attribute value
```

### **4. Handling Implicit Waits**

```python
driver.implicitly_wait(10)
```

#### **What does **``** do?**

`implicitly_wait(10)` tells Selenium to wait up to 10 seconds for an element to be found before throwing an exception. This is useful for handling elements that take time to load dynamically.

### **5. Handling Alerts**

```python
alert = driver.switch_to.alert
print(alert.text)  # Get alert text
alert.accept()  # Accept alert
alert.dismiss()  # Dismiss alert
```

### **6. Handling Frames and Windows**

```python
driver.switch_to.frame("frame_name")  # Switch to a frame
driver.switch_to.default_content()  # Switch back to main page
driver.switch_to.window("window_handle")  # Switch between windows
```

---

## **7. Automating a Login Test Case**

```python
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver  # `yield` allows returning a generator and executes teardown code after the test
    driver.quit()
```

#### **What is **``** in Python?**

`yield` in a fixture allows the test to run while keeping the WebDriver instance active, and once the test is done, the WebDriver is properly closed using `driver.quit()`.

```python
def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"
```

---

## **8. Taking Screenshots**

```python
driver.save_screenshot("screenshot.png")
```

---

## **9. Closing the Browser**

```python
driver.quit()
```

---

