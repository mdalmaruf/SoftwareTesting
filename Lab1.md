# Lab 1: Secure Password Generator

## **Objective**
In this lab, you will develop a Python program that generates secure passwords based on user-defined criteria, such as length, number of letters, digits, and special characters. You will also gain hands-on experience with input validation and handling randomness using the `random` module.

## **Learning Outcomes**
By the end of this lab, you will be able to:

- Understand and implement password generation logic.
- Use the `random` module to generate random letters, digits, and special characters.
- Validate user inputs to ensure correct values.
- Apply basic file operations to save generated passwords.
- Practice using GitHub for version control and project submission.

---

## **Getting Started**

### **Step 1: Setup**
1. Ensure Python is installed on your system (version 3.6 or later).
2. Open your preferred code editor (VS Code, PyCharm, etc.).
3. Create a new Python file named `password_generator.py`.

---

## **Step 2: Understanding the `random` Module**

Python's `random` module allows us to generate random values, which is essential for our password generator. Let's try a small activity to understand how it works.

### **Activity: Generating Random Characters**

```python
import random
import string

# Generate a random letter
random_letter = random.choice(string.ascii_letters)
print(f"Random letter: {random_letter}")

# Generate a random digit
random_digit = random.choice(string.digits)
print(f"Random digit: {random_digit}")

# Generate a random special character
random_special = random.choice(string.punctuation)
print(f"Random special character: {random_special}")
```

**Expected Output Example:**
```bash
Random letter: K
Random digit: 5
Random special character: $
```

**Task:**  
- Modify the code to generate multiple random characters of each type.
- Combine the generated values into a random string.

---

## **Step 3: Plan Your Password Generator**

Before writing the complete program, think about how you'll handle the following:

1. **User Inputs:**  
   - Ask for the total password length.
   - Ask for the number of letters, digits, and special characters.

2. **Input Validation:**  
   - Ensure inputs are valid (e.g., positive numbers, within acceptable ranges).
   - Check if the sum of letters, digits, and special characters does not exceed the total length.

3. **Password Construction:**  
   - Use the `random` module to generate components.
   - Shuffle the elements to create a strong password.

---

## **Step 4: Basic Password Generation Steps**

Follow these simple steps to create your password generator:

1. **Prompt the user for input.**
2. **Generate random characters based on user input.**
3. **Combine all parts and shuffle them.**
4. **Display the generated password.**
---

## **Step 5: Submission Instructions**

Once you have completed your lab, follow these steps to submit your work:

1. **Create a GitHub Repository:**
   - Go to [GitHub](https://github.com) and create a new repository named `SecurePasswordGenerator`.
   - Clone the repository to your local machine.

2. **Upload Your Code:**
   ```bash
   git add .
   git commit -m "Lab 1: Secure Password Generator"
   git push origin main
   ```

3. **Record a Video Demonstration:**
   - Walk through your code and demonstrate its functionality.
   - Upload the video to YouTube or a cloud storage service.

4. **Submit the GitHub Repository Link and Video Link.**

---

## **Checklist Before Submission**
- [ ] Ensure the password meets the user's requirements.
- [ ] Validate inputs properly.
- [ ] Save the password to a file.
- [ ] Document your code with comments.
- [ ] Successfully push your code to GitHub.
- [ ] Group Video Presentation about Lab1 

---

# Program Structure
```python
import random
import string

# Function to get user input (skeleton)
def get_user_input(prompt, min_value, max_value):
    # Implement logic to get valid user input within a range
    pass

# Function to generate a password (skeleton)
def generate_password(length, num_letters, num_digits, num_specials):
    # Ensure total requested characters do not exceed length
    # Generate required characters (letters, digits, specials)
    # Fill remaining characters
    # Shuffle and return password
    pass

# Main function (skeleton)
def main():
    print("\n--- Secure Password Generator ---\n")

    # Step 1: Get user inputs for password length and character distribution

    # Step 2: Validate user inputs

    # Step 3: Generate the password

    # Step 4: Display the generated password

    # Step 5: Save password to file

# Entry point of the script
if __name__ == "__main__":
    main()

```
