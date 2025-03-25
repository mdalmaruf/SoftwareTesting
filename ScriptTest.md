import unittest                                        # ✅ Built-in Python testing framework
from time import sleep                                 # ⏳ Adds wait between steps
from selenium import webdriver                         # 🌐 Main Selenium WebDriver
from selenium.webdriver.common.action_chains import ActionChains  # 🤖 For drag-and-drop
from selenium.webdriver.support.ui import Select       # 🔽 For dropdown menus
from webdriver_manager.chrome import ChromeDriverManager  # 🧰 Manages ChromeDriver automatically
from selenium.webdriver.common.by import By            # 🔍 Modern way to locate elements

from selenium.webdriver.support.ui import WebDriverWait        # 🕐 Explicit wait
from selenium.webdriver.support import expected_conditions as EC  # ✅ Wait conditions

class SeleniumTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()                 # 🚘 Launch Chrome browser
        cls.driver.maximize_window()                    # 🔍 Maximize for full visibility
        sleep(2)

    # ---------------- Test 1 -------------------
    def test01_simple_alert(self):
        driver = self.driver
        driver.get("https://demoqa.com/alerts")         # 🌐 Load the alert page
        sleep(2)

        driver.find_element("id", "alertButton").click()  # 👆 Clicks alert trigger
        alert = driver.switch_to.alert                  # 🔄 Switch to alert popup
        print("Alert Text: ", alert.text)               # 📝 Print alert message
        alert.accept()                                  # ✅ Click "OK"

    # ---------------- Test 2 -------------------
    def test02_confirmation_alert(self):
        driver = self.driver
        driver.get("https://demoqa.com/alerts")
        sleep(2)

        driver.find_element(By.ID, "confirmButton").click()  # 👆 Trigger confirmation alert
        alert = driver.switch_to.alert
        print("Confirmation Alert Text: ", alert.text)
        alert.dismiss()                                  # ❌ Click "Cancel"

        result = driver.find_element(By.ID, "confirmResult").text  # 🔍 Get confirmation result
        self.assertEqual(result, "You selected Cancel")   # ✅ Check correct output

    # ----------- Improved version of Test 2 ------------
    def test02_confirmation_alert_scroll(self):
        driver = self.driver
        driver.get("https://demoqa.com/alerts")
        wait = WebDriverWait(driver, 10)                  # 🕒 Wait up to 10s

        confirm_button = wait.until(                      # ✅ Wait until button is clickable
            EC.element_to_be_clickable((By.ID, "confirmButton"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", confirm_button)  # 🔽 Scroll into view
        sleep(1)

        confirm_button.click()                            # 👆 Click
        alert = driver.switch_to.alert
        print("Confirmation Alert Text: ", alert.text)
        alert.dismiss()

        result = driver.find_element(By.ID, "confirmResult").text
        self.assertEqual(result, "You selected Cancel")   # ✅ Assert expected message

    # ---------------- Test 3 -------------------
    def test03_prompt_alert(self):
        driver = self.driver
        driver.get("https://demoqa.com/alerts")
        sleep(1)

        driver.find_element(By.ID, "promtButton").click()  # 👆 Trigger prompt alert
        alert = driver.switch_to.alert
        self.assertIn("Please enter your name", alert.text)  # 🔍 Confirm prompt is correct
        alert.send_keys("Maruf")                          # ✍️ Input name
        alert.accept()
        result = driver.find_element(By.ID, "promptResult").text
        self.assertIn("Maruf", result)                    # ✅ Assert name appears

    # ---------------- Test 4 -------------------
    def test04_drag(self):
        driver = self.driver
        driver.get("https://jqueryui.com/draggable/")
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))  # 🖼️ Switch into iframe

        draggable = driver.find_element(By.ID, "draggable")  # 🎯 Get draggable box
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(draggable, 100, 100).perform()  # 🧲 Move by offset
        location = draggable.location
        self.assertTrue(location['x'] > 0 and location['y'] > 0)  # ✅ Check moved position

    # ---------------- Test 5 -------------------
    def test05_drag_drop(self):
        driver = self.driver
        driver.get("https://jqueryui.com/droppable/")
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

        source = driver.find_element(By.ID, "draggable")     # 📦 Source element
        target = driver.find_element(By.ID, "droppable")     # 🎯 Drop target
        ActionChains(driver).drag_and_drop(source, target).perform()
        self.assertEqual("Dropped!", target.text)            # ✅ Confirm drop success

    # ---------------- Test 6 -------------------
    def test06_dropdown_by_index(self):
        driver = self.driver
        driver.get("http://demo.guru99.com/test/newtours/register.php")
        sleep(2)

        dropdown = Select(driver.find_element(By.NAME, "country"))  # 🔽 Country dropdown
        dropdown.select_by_index(6)                                 # 📌 Select 6th option
        self.assertEqual("ANTARCTICA", dropdown.first_selected_option.text)

    # ---------------- Test 7 -------------------
    def test07_dropdown_by_value(self):
        driver = self.driver
        driver.get("http://demo.guru99.com/test/newtours/register.php")
        sleep(2)

        dropdown = Select(driver.find_element(By.NAME, "country"))
        dropdown.select_by_value("AUSTRIA")                         # 🔤 Select by value
        self.assertEqual("AUSTRIA", dropdown.first_selected_option.text)

    # ---------------- Test 8 -------------------
    def test08_multiple_windows(self):
        driver = self.driver
        driver.get("https://demoqa.com/browser-windows")
        sleep(1)

        driver.find_element(By.ID, "windowButton").click()          # 👆 Open new window
        handles = driver.window_handles
        self.assertEqual(len(handles), 2)                           # ✅ Confirm new window opened

        driver.switch_to.window(handles[1])                         # 🔄 Switch to new window
        self.assertIn("This is a sample page", driver.page_source)  # 🔍 Check page content
        driver.close()
        driver.switch_to.window(handles[0])                         # 🔁 Return to main window

    # ---------------- Test 9 -------------------
    def test09_screenshot(self):
        driver = self.driver
        driver.get("http://www.google.com")
        sleep(2)

        screenshot_path = "google_homepage.png"
        driver.save_screenshot(screenshot_path)                    # 📸 Take screenshot
        print(f"Screenshot saved at {screenshot_path}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()                                          # ❌ Close browser


if __name__ == "__main__":
    unittest.main()                                                # ▶️ Run the test suite
