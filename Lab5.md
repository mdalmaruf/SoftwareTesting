# Lab 5: Selenium Python API for Element Interaction

Welcome to Lab 5! This lab focuses on using the Selenium Python API to automate a shopping workflow on the Magento e-commerce platform. Below, you’ll find detailed instructions and steps to complete the lab successfully.

---

## **Objective**
Learn and practice:
- Automating web interactions using Selenium.
- Writing test scripts to navigate, interact with web elements, and assert results.
- Working collaboratively in pairs to develop and document test automation scripts.

---
## **What is Selenium Python API?**
Selenium is a powerful open-source tool used for automating web browsers. It allows developers and testers to write scripts in various programming languages, including Python, to simulate user interactions with web applications. The **Selenium Python API** provides methods to:
- Locate web elements.
- Perform actions such as clicking, typing, or selecting.
- Extract data for validation.
- Automate workflows across different browsers like Chrome, Firefox, and Edge.

### **How Selenium Works**
- **WebDriver**: Acts as a bridge between your Python script and the web browser.
   - Example: ChromeDriver enables Selenium to interact with Google Chrome.
- **Browser Automation**: Uses commands to interact with web elements like buttons, text fields, and dropdowns.
- **Locators**: Identifies web elements using:
   - ID
   - Name
   - XPath
   - CSS Selector
   - Link Text
- **Assertions**: Validates expected outcomes in automated workflows.

## **Setup Instructions**
1. **Install Dependencies**:
   - Ensure Python and pip are installed on your system.
   - Install Selenium using pip:
     ```bash
     pip install selenium
     ```
   - Download the Chrome WebDriver matching your Chrome version and add it to your system’s PATH.

2. **Using PyCharm**:
   - Open PyCharm and create a new project for Lab 5:
     - Go to **File > New Project**.
     - Name the project `Lab5_GroupN` (replace `N` with your group number).
   - Inside the project, create a new Python file:
     - Name the file `Lab5_firstname1_firstname2.py` (replace with both group members' names).
   - Set up a virtual environment if necessary:
     - Go to **File > Settings > Project > Python Interpreter** and select or create a new virtual environment.
   - Install Selenium in the PyCharm terminal:
     ```bash
     pip install selenium
     ```

3. **Group Formation**:
   - Work in pairs to complete this lab.
   - Both partners must actively participate in coding and recording tasks.

---

## **Program Requirements**
### **Workflow Overview**
Automate the following shopping workflow:
1. Navigate to [Magento Demo Website](https://magento.softwaretestingboard.com/).
2. Perform shopping steps:
   - **Women > Tops > Hoodies & Sweatshirts**.
   - Filter products by:
     - Style: Pullover
     - Size: M
     - Price: $50.00 - $59.99
     - Color: Purple
     - Material: Polyester
   - Select a product and add it to the cart.
   - Proceed to checkout and assert the order summary.

3. Close the browser after completing the automation.

---

## **Steps to Complete the Lab**

### 1. **Navigate to the Product Page**
- Use Selenium’s `find_element` method to locate and click:
  - **"Women" menu**.
  - **"Tops" category**.
  - **"Hoodies & Sweatshirts"**.

### 2. **Filter Products**
- Apply filters for style, size, price, color, and material:
  - Use **XPath** or **CSS Selectors** to locate dropdowns or checkboxes.
  - Example code to select a filter:
    ```python
    style_filter = driver.find_element(By.XPATH, "//span[text()='Pullover']")
    style_filter.click()
    ```

### 3. **Select and Add to Cart**
- Select a filtered product and add it to the cart:
  - Handle **frames** if required:
    ```python
    driver.switch_to.frame("frame_name")
    add_to_cart_button = driver.find_element(By.ID, "add-to-cart")
    add_to_cart_button.click()
    driver.switch_to.default_content()
    ```

### 4. **View Cart and Proceed to Checkout**
- Click the cart icon and proceed to checkout:
  ```python
  cart_icon = driver.find_element(By.ID, "cart-icon")
  cart_icon.click()
  checkout_button = driver.find_element(By.XPATH, "//button[text()='Proceed to Checkout']")
  checkout_button.click()
  ```
### 5. **Assert the Order Summary**
- Validate the product in the order summary using `assert`:
  ```python
  order_summary = driver.find_element(By.CLASS_NAME, "order-summary")
  assert "Pullover" in order_summary.text, "Order summary does not include the selected item"
  ```
### 5. **Close the Browser**
- Ensure the browser closes after the test completes:
  ```bash
  driver.quit()
  ```

## **General Requirements**
- **Test-Case Fixtures**: Write separate test cases for each step to maintain modularity.
- **Comments**: Add meaningful comments explaining your code and element selections.
- **Video Recording**:
  - Showcase the workflow on the Magento website.
  - Explain your code and logic during the recording.
- **File Submission**: Zip your project folder and submit as required.

---

## **Example Code Structure**
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# Test Case 1: Navigate to Product Page
def test_navigate_to_product_page(driver):
    driver.get("https://magento.softwaretestingboard.com")
    driver.find_element(By.LINK_TEXT, "Women").click()
    driver.find_element(By.LINK_TEXT, "Tops").click()
    driver.find_element(By.LINK_TEXT, "Hoodies & Sweatshirts").click()

# Test Case 2: Apply Filters
def test_apply_filters(driver):
    driver.find_element(By.XPATH, "//span[text()='Pullover']").click()
    driver.find_element(By.XPATH, "//span[text()='M']").click()
    driver.find_element(By.XPATH, "//span[text()='Purple']").click()

# Test Case 3: Add to Cart and Assert
def test_add_to_cart(driver):
    driver.find_element(By.XPATH, "//button[text()='Add to Cart']").click()
    cart_icon = driver.find_element(By.ID, "cart-icon")
    cart_icon.click()
    assert "Pullover" in driver.find_element(By.CLASS_NAME, "order-summary").text

```




# Tips and Best Practices

## **Tips and Best Practices**
1. Use **ChroPath** to identify precise locators.
2. Modularize your code by dividing the workflow into separate test cases.
3. Verify all selectors and test thoroughly to ensure accuracy.
4. Collaborate effectively with your partner and document task distribution.

---

## **Common Challenges and Solutions**

### **Issue: Unable to locate an element**
- **Solution**: Use ChroPath to refine the locator and ensure the page is fully loaded before interaction.

### **Issue: Filters not applying correctly**
- **Solution**: Use explicit waits to ensure all elements are interactable:
  ```python
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC

  element = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, "//button[text()='Add to Cart']"))
  )
  ```
# Sample Working Example:
   ```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MagentoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH
        cls.driver.maximize_window()
        cls.driver.get("https://magento.softwaretestingboard.com/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_navigate_to_product_page(self):
        """Navigate to Women -> Tops -> Hoodies & Sweatshirts"""
        print("Navigating to Women -> Tops -> Hoodies & Sweatshirts")
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Women"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Tops"))).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[text()='Category']"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Hoodies & Sweatshirts')]"))
        ).click()

    def test_02_apply_filters(self):
        """Apply Filters"""
        print("Applying filters: Pullover, Size: M, Color: Purple")
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Pullover']"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='M']"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Purple']"))).click()

    def test_03_add_to_cart(self):
        """Select Product and Add to Cart"""
        print("Selecting a product and adding it to the cart")
        driver = self.driver
        product = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'product-item-link')]"))
        )
        product.click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to Cart']"))
        ).click()

    def test_04_checkout(self):
        """View Cart and Proceed to Checkout"""
        print("Proceeding to checkout")
        driver = self.driver
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'showcart')]"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@title='Proceed to Checkout']"))
        ).click()

    def test_05_validate_order_summary(self):
        """Validate Order Summary"""
        print("Validating the order summary")
        driver = self.driver
        summary = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "block-summary"))
        )
        assert "Pullover" in summary.text, "Order Summary does not contain the selected product"


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(MagentoTest("test_01_navigate_to_product_page"))
    suite.addTest(MagentoTest("test_02_apply_filters"))
    suite.addTest(MagentoTest("test_03_add_to_cart"))
    suite.addTest(MagentoTest("test_04_checkout"))
    suite.addTest(MagentoTest("test_05_validate_order_summary"))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


   ```
---

## Explanation

### **Explicit TestSuite**
- The `unittest.TestSuite()` is used to explicitly specify the order of test execution.
- This approach ensures that tests are executed in the desired sequence, irrespective of the default alphabetical sorting.

### **Naming Conventions**
- Each test method is prefixed with `test_01_`, `test_02_`, etc., for clarity and to indicate the intended execution order.
- This naming convention helps:
  - Maintain readability.
  - Ensure consistent execution order when relying on default sorting.

### **Sequential Execution**
- The `TestSuite` ensures that tests are executed in the exact order they are added to the suite.
- This is especially important when:
  - Tests are interdependent.
  - The outcome of one test affects the subsequent tests.

---




## Other Issues You may Find

- **Hover Issues**  
Elements like the "Tops" menu are hidden until you hover over the parent menu ("Women"). Selenium's default click action does not emulate hovering, so the submenu remains hidden, causing the test to fail.

- **Advertisement Overlap**  
Ads are dynamically placed on the page and can obstruct elements, making them unclickable.

## Solution: Using Hover Actions and Scroll Handling

To address these challenges, the following solutions are implemented:

1. **Simulating Hover Actions**  
Selenium's `ActionChains` class is used to hover over menu items, ensuring dropdowns are displayed before clicking.

2. **Scrolling to Elements**  
A `scroll_into_view` method ensures hidden elements are scrolled into the viewport, making them interactable and avoiding ad interference.

3. **Waiting for Elements**  
Explicit waits (`WebDriverWait`) ensure elements are interactable before attempting any actions.

## Example Solution: `test_01_navigate_to_product_page`

Below is an example test case that demonstrates how to navigate through hover-dependent menus while handling obstructive advertisements.

### Code Example

```python
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class MagentoTest(unittest.TestCase):

 @classmethod
 def setUpClass(cls):
     """Set up the WebDriver instance before running any tests."""
     cls.driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH
     cls.driver.maximize_window()
     cls.driver.get("https://magento.softwaretestingboard.com/")

 @classmethod
 def tearDownClass(cls):
     """Quit the WebDriver instance after all tests."""
     cls.driver.quit()

 def hover_element(self, element):
     """Performs a hover action on the given element."""
     actions = ActionChains(self.driver)
     actions.move_to_element(element).perform()

 def scroll_into_view(self, element):
     """Scrolls the element into view to ensure it's interactable."""
     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

 def test_01_navigate_to_product_page(self):
     """Navigate to Women -> Tops -> Hoodies & Sweatshirts."""
     print("Navigating to Women -> Tops -> Hoodies & Sweatshirts")
     driver = self.driver

     # Hover on "Women" to reveal the dropdown
     women_menu = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Women")))
     self.hover_element(women_menu)

     # Click on "Tops"
     tops_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Tops")))
     tops_menu.click()
     time.sleep(2)

     # Scroll to "Category" and expand it
     category_filter = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "//div[text()='Category']"))
     )
     self.scroll_into_view(category_filter)
     category_filter.click()

     # Click on "Hoodies & Sweatshirts" under Category
     hoodies_link = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Hoodies & Sweatshirts')]"))
     )
     self.scroll_into_view(hoodies_link)
     hoodies_link.click()


if __name__ == "__main__":
 suite = unittest.TestSuite()
 suite.addTest(MagentoTest("test_01_navigate_to_product_page"))

 runner = unittest.TextTestRunner(verbosity=2)
 runner.run(suite)
```
## Key Highlights in the Solution

### Hover Action
- **`ActionChains`** is used to hover over the "Women" menu, making the "Tops" submenu visible.

### Scroll Handling
- The **`scroll_into_view`** method ensures elements like the "Category" filter and "Hoodies & Sweatshirts" are scrolled into view before interaction.

### Explicit Waits
- **`WebDriverWait`** ensures elements are interactable before clicking, reducing flaky tests caused by dynamic page loads.



# Submission Guidelines

## **File Format**
- Submit `Lab5_firstname1_firstname2.py` following naming conventions.

## **Video**
- Record a clear demonstration of your code and test execution.

## **Upload**
- Attach the zipped project folder to the assignment folder.
