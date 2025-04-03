
# INFT 1207 - Test Automation of Banking Project

## Overview
This project involves automated testing of a **banking demo website** using **Selenium WebDriver with Python**. It replicates a corporate setting where the team is responsible for testing multiple banking modules before release.

## Demo Website
- **Website:** [http://demo.guru99.com/V4/](http://demo.guru99.com/V4/)
- **Login Credentials:**  
  - Visit [http://demo.guru99.com](http://demo.guru99.com) and enter your email to receive temporary credentials.  
  - Example credentials:  
    - **User ID:** mngr160860  
    - **Password:** pumagEm  
- Credentials are valid for **20 days**. Generate new ones if needed.

---

## Project Scope
Your team will automate the following **Manager Role Modules**:

1. **New Customer**  
2. **Edit Customer**  
3. **Delete Customer**  
4. **New Account**  
5. **Edit Account**  
6. **Delete Account**  
7. **Balance Enquiry**  
8. **Mini Statement**  
9. **Customized Statement**

Each module contains specific **test cases** assigned equally among the team members.

---

## Submission Requirements

### 1. Group Project Submission (Due Date: Week 14)
One submission per group with the following deliverables:
- **Source Code:** Zipped folder named:  
  `INFT 1207 - Group#Project.zip`
- **Test Case Suite:** Excel sheet with results and pass/fail status:  
  `INFT 1207 - Group#TestCasesuitesolution`
- **HTML Test Results:** Exported from Selenium tests.
- **Bug Tracker Report:**  
  `INFT 1207 - Group#Bug Tracker Report`
- **Video Recordings:**  
  - Single recording: `INFT 1207 - Group#ProjectRecording`  
  - OR individual recordings: `INFT 1207 - Group#Firstname`
- **Project Report:**  
  PDF following guidelines (detailed below), named:  
  `INFT 1207 - Group#Projectreport`

---

## Project Report Guidelines (Total Marks = 20, Worth = 10%)
The project report must adhere to the following format:

- **Length:** 7-15 pages  
- **Formatting:**
  - **Titles:** Arial, 14pt, Bold  
  - **Sub-Titles:** Arial, 12pt, Bold, Italics  
- **Cover Page:**  
  - Title of the project, Group no., Group members with IDs  
  - Group logo (design your own), Course code & name, DC logo  
- **Footer:** Page number and date  
- **Table of Contents:** 



### Report Content
1. **Purpose of the Project**
2. **Scope of the Project**
3. **Software Used**
4. **Naming Convention Used in Programs**
5. **Distribution of Work Among Team Members**
6. **Approach Used by the Team**
7. **Module-wise Implementation Details**
8. **Challenges Faced by the Team**
9. **Resolutions Adopted**
10. **Appendix A:** References (web links, books, etc.)
11. **Appendix B:** Project Management Details  
  - **Team Leader:** Summary of contributions in table format:
    ```
    Team Member   Topic   Contribution Summary
    ```

---

## Peer Feedback (Total Marks = 10, Worth = 5%)
Each member must submit **peer feedback** to evaluate their team members by the due date.  

### Feedback Guidelines
1. **Timely Submission:**  
 - Earns **40%** of 10 marks.  
 - **Late submission penalty:** 25% deduction.
2. **Peer Ratings:**  
 - **60% of the marks** will be earned through peer ratings.  
 - The **average rating** from peers will be used to calculate marks.  

**Note:**  
- Failure to submit your peer feedback will result in **zero marks** for this portion, regardless of other members’ ratings.
- The feedback submission is individual, and all ratings must reflect the entire project timeline.

---

## Project Workflow

### Phase 1: Group Formation (Weeks 6-7)
- Form a group of up to **4 members**.
- Divide the 100 test cases evenly among members:
- New Customer: 28 cases  
- Edit Customer: 20 cases  
- Delete Customer: 8 cases  
- New Account: 16 cases  
- Edit Account: 8 cases  
- Delete Account: 8 cases  
- Balance Enquiry: 7 cases  
- Mini Statement: 8 cases  
- Customized Statement: 17 cases  

### Phase 2: Development and Testing (Weeks 8-12)
- Implement a **menu-driven program (`testsuite.py`)** to execute test cases for different modules.
- Use **Selenium WebDriver** with Python to automate testing.
- Record results in the **Test Case Suite Excel sheet** and export **HTML reports**.

### Phase 3: Bug Tracking and Reporting
- Log failed test cases in the **Bug Tracker Report** for further resolution.
- Prepare individual video recordings explaining your contribution and code.

### Phase 4: Final Submission and Demo (Week 14)
- Present the project demo during class, where all members must attend and participate.
- Each member may be asked to **execute specific test cases** during the demo.

---

## Grading Criteria (Total: 100 Marks)
| **Criteria**                                 | **Marks** |
|----------------------------------------------|-----------|
| Naming convention followed                   | 5         |
| Test Case Execution (0.42 marks per case)    | 50        |
| Completed Test Case Suite (Excel)            | 20        |
| HTML Test Results                            | 10        |
| Video Recordings (Single: 10 or 2.5 each)    | 10        |
| Bug Tracker Report                           | 5         |

---

## How to Run the Project
1. Install **Python** and **Selenium WebDriver**.
2. Clone the repository and navigate to the project folder.
3. Install required dependencies using:
   ```bash
   pip install selenium
   ```
4. Run the menu-driven test suite using:
  ```bash
  python testsuite.py
  ```
5. Export the test results and generate HTML reports.

# Example of New Customer Page:

```python
# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestNewCustomer():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_login(self):
        self.driver.get("https://demo.guru99.com/V4/")
        #self.driver.set_window_size(1534, 912)
        self.driver.maximize_window()
        self.driver.find_element(By.NAME, "uid").click()
        self.driver.find_element(By.NAME, "uid").send_keys("mngr615627")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("EmUqujY")
        self.driver.find_element(By.NAME, "btnLogin").click()
        #self.driver.find_element(By.CSS_SELECTOR, ".heading3 > td").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".heading3 > td").text == "Manger Id : mngr615627"

    # def NC1(self):
           #check the excel file provided in the Project Submission Folder 
    def NC2(self):
        self.driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        self.driver.set_window_size(1534, 912)
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("1234")
        self.driver.find_element(By.ID, "message").click()
        assert self.driver.find_element(By.ID, "message").text == "Numbers are not allowed"

 

   # def NC3(self):
      #check the excel file provided in the Project Submission Folder

   # def NC4(self):
      #check the excel file provided in the Project Submission Folder 

```


