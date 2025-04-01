**Selenium with Python unittest - Detailed Tutorial**

The following code explains the structure, components, and functionality of three Selenium-based automation scripts written using Python's `unittest` framework. The examples include handling checkboxes, radio buttons, and date pickers.

---

```


### 1. **Common Imports and Setup**
```python
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
```

- `unittest`: Built-in Python module for writing and running tests.
- `sleep`: Pauses execution for specified seconds; helps wait for UI to load.
- `webdriver`: Provides an interface to interact with the browser.
- `By`: Used to locate elements using different strategies (ID, NAME, CLASS_NAME, etc.).
- `ChromeDriverManager`: Automatically manages and installs the correct ChromeDriver.
```python
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class CheckboxDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        sleep(2)

    def test01_checkbox(self):
        driver = self.driver
        driver.get("http://demo.guru99.com/test/radio.html")
        sleep(5)

        # Locate checkboxes
        checkbox1 = driver.find_element(By.ID, "vfb-6-0")
        checkbox2 = driver.find_element(By.ID, "vfb-6-1")
        checkbox3 = driver.find_element(By.ID, "vfb-6-2")

        # Click checkbox 2 and 3
        checkbox2.click()
        sleep(1)
        checkbox3.click()
        sleep(1)

        # Assertions
        self.assertTrue(checkbox2.is_selected())
        self.assertTrue(checkbox3.is_selected())
        self.assertFalse(checkbox1.is_selected())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

---



  
### 2. **Checkbox Handling: `CheckboxDemo`**
This test interacts with checkboxes on a sample webpage.

#### Setup:
```python
@classmethod
def setUpClass(cls):
    cls.driver = webdriver.Chrome()
    cls.driver.maximize_window()
    sleep(2)
```
- Initializes the Chrome browser only once before all tests.
- Maximizes the browser window for better visibility.

#### Test Method:
```python
def test01_checkbox(self):
    driver = self.driver
    driver.get("http://demo.guru99.com/test/radio.html")
    sleep(5)
```
- Opens the test webpage.

##### Checkbox Actions:
```python
checkbox1 = driver.find_element(By.ID, "vfb-6-0")
checkbox2 = driver.find_element(By.ID, "vfb-6-1")
checkbox3 = driver.find_element(By.ID, "vfb-6-2")
checkbox2.click()
checkbox3.click()
```
- Locates checkboxes by ID and simulates clicks.

##### Assertions:
```python
self.assertTrue(checkbox2.is_selected())
self.assertTrue(checkbox3.is_selected())
self.assertFalse(checkbox1.is_selected())
```
- Validates selection status of each checkbox.
```python
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class RadioButtonDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        sleep(2)

    def test01_radiobutton(self):
        driver = self.driver
        driver.get("http://demo.guru99.com/test/radio.html")
        sleep(5)

        # Locate radio buttons
        option1 = driver.find_element(By.ID, "vfb-7-1")
        option3 = driver.find_element(By.ID, "vfb-7-3")

        # Select option1
        option1.click()
        self.assertTrue(option1.is_selected())
        sleep(1)

        # Select option3
        option3.click()
        self.assertTrue(option3.is_selected())
        self.assertFalse(option1.is_selected())  # Only one selected at a time

        # Get all radio buttons
        radio_buttons = driver.find_elements(By.NAME, "vfb-7")
        print(f"Total radio buttons found: {len(radio_buttons)}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
```  
---


  
### 3. **Radio Button Handling: `RadioButtonDemo`**

#### Setup:
Same as checkbox class.

#### Test Method:
```python
def test01_radiobutton(self):
    driver.get("http://demo.guru99.com/test/radio.html")
```
- Opens the demo page containing radio buttons.

##### Radio Button Actions:
```python
option1 = driver.find_element(By.ID, "vfb-7-1")
option3 = driver.find_element(By.ID, "vfb-7-3")
option1.click()
option3.click()
```
- Clicking on option3 deselects option1 since only one radio can be selected.

##### Assertions:
```python
self.assertTrue(option3.is_selected())
self.assertFalse(option1.is_selected())
```

##### Count All Radio Buttons:
```python
radio_buttons = driver.find_elements(By.NAME, "vfb-7")
print(f"Total radio buttons found: {len(radio_buttons)}")
```
- Useful for debugging or verifying number of elements.

---

### 4. **Date Picker Handling: `DatePickingDemo`**

#### Setup:
Same as above.

### Test Case 1: Pick a Single Date
```python
driver.get("https://jqueryui.com/datepicker/")
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))
date_input = driver.find_element(By.ID, "datepicker")
date_input.click()
```
- Switches to iframe before interacting with calendar widget.

##### Select a Date:
```python
all_dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//a")
for date in all_dates:
    if date.text == "15":
        date.click()
        break
```

##### Assertion:
```python
selected_date = date_input.get_attribute("value")
self.assertTrue(len(selected_date) > 0)
```

### Test Case 2: Pick a Date Range
```python
driver.get("https://jqueryui.com/datepicker/#date-range")
driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))
```

##### From and To Dates:
```python
from_date_input = driver.find_element(By.ID, "from")
to_date_input = driver.find_element(By.ID, "to")
from_date_input.click()
driver.find_element(By.LINK_TEXT, "20").click()
to_date_input.click()
driver.find_element(By.LINK_TEXT, "26").click()
```

##### Validate:
```python
from_selected = from_date_input.get_attribute("value")
to_selected = to_date_input.get_attribute("value")
self.assertIn("20", from_selected)
self.assertIn("26", to_selected)
```

---

### 5. **Teardown for All Classes**
```python
@classmethod
def tearDownClass(cls):
    cls.driver.quit()
```
- Closes the browser after all test cases have run.
```python  
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class DatePickingDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        sleep(2)

    def test01_date_picking(self):
        driver = self.driver
        driver.get("https://jqueryui.com/datepicker/")
        sleep(5)

        driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))
        date_input = driver.find_element(By.ID, "datepicker")
        date_input.click()

        # Select a specific date (e.g., 15)
        all_dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//a")
        for date in all_dates:
            if date.text == "15":
                date.click()
                break

        selected_date = date_input.get_attribute("value")
        print(f"Selected Date: {selected_date}")
        self.assertTrue(len(selected_date) > 0)

        driver.switch_to.default_content()
        sleep(2)

    def test02_date_picking(self):
        driver = self.driver
        driver.get("https://jqueryui.com/datepicker/#date-range")
        sleep(5)

        driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

        from_date_input = driver.find_element(By.ID, "from")
        to_date_input = driver.find_element(By.ID, "to")

        from_date_input.click()
        driver.find_element(By.LINK_TEXT, "20").click()
        sleep(1)

        to_date_input.click()
        driver.find_element(By.LINK_TEXT, "26").click()
        sleep(1)

        from_selected = from_date_input.get_attribute("value")
        to_selected = to_date_input.get_attribute("value")

        print(f"From Date: {from_selected}")
        print(f"To Date: {to_selected}")
        self.assertIn("20", from_selected)
        self.assertIn("26", to_selected)

        driver.switch_to.default_content()
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
  
```

           
---


