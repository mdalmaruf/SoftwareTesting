# Lab 2: Reading List Manager

## Lab Overview

This project is part of **Lab 2: Test Case Design** for INFT 1207 – Software Testing and Automation. The goal of this lab is to create a Python program that manages a reading list by adding, listing, and searching books. The data will be stored in a CSV file.

---

## Project Setup Instructions

### Step 1: Set Up PyCharm Project

1. **Open PyCharm** and create a new Python project by navigating to **File -> New Project**.
2. Name the project `Lab2_GroupN` (replace `N` with your group number).
3. Create a Python file and name it `Lab2_firstname1_firstname2.py` (replace `firstname1` and `firstname2` with your names).

### Step 2: Create `books.csv` File

1. In the project directory, create a new file named `books.csv`.
2. This file will store the book information in the following CSV format:
   ```csv
   Title,Author,Year
   1Q84,Haruki Murakami,2009
   The Picture of Dorian Gray,Oscar Wilde,1890
   ```
3. You can add more entries or modify the file for testing purposes as needed.

### Code Overview
In this lab, you will develop a Python program that can:

1. Add a book to the reading list.
2. List all books in a user-friendly format.
3. Search for a specific book by title.
4. Store and retrieve the data from books.csv.

### Example Code
Create the file named `reading_list.py` to write the main functionalities of the program.
Below is an example Python code that provides the basic structure for adding, listing, and searching books.

```python
import csv

# Function to add a book to the reading list
def add_book(title, author, year):
    with open('books.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, author, year])

# Function to list all books
def list_books():
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f'Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')

# Function to search for a book by title
def search_book(title):
    with open('books.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() == title.lower():
                print(f'Found: Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
                return
        print('Book not found')

# Menu loop
def menu():
    while True:
        print("\n1. Add Book\n2. List Books\n3. Search Book\n4. Quit")
        choice = input("Select an option: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter year of publication: ")
            add_book(title, author, year)
        elif choice == '2':
            list_books()
        elif choice == '3':
            title = input("Enter book title to search: ")
            search_book(title)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    menu()

```


### Student Tasks


# Student Tasks

## Task 1: Enhance the Functionality
You are required to enhance the current functionality by:

- **Error Handling**: Ensure the program handles input errors (e.g., invalid year, missing fields, file errors).
- **Delete a Book**: Implement a feature to delete a book from the CSV file.
- **Refactor the Code**: Organize the code by separating the file operations into utility functions for better code readability.

## Task 2: Test Case Design
Create another file named `test_reading_list.py` to write the test cases.
Write at least 10 test cases using Python’s `unittest` framework to verify the following:

- Adding a new book with valid and invalid inputs.
- Listing all books.
- Searching for existing and non-existing books.

### Example Test Case:

```python
import unittest
from reading_list import add_book, list_books, search_book

class TestReadingList(unittest.TestCase):
    def test_add_book(self):
        add_book("Test Book", "Author Name", 2022)
        # Assert if the book is added (by manually checking CSV or creating validation logic)

    def test_search_book(self):
        search_book("Test Book")
        # Assert the output of the search
    
    # More test cases to be added...

if __name__ == '__main__':
    unittest.main()
```


## Task 3: Test Execution
- Run all your test cases and ensure they pass.
- Submit your test report along with the test case design table.

## Task 4: Teamwork Component
- Both partners must submit a video recording where you explain the code line-by-line and show the program in action.
- Each partner should mention how the tasks were distributed between them.

## Submission Guidelines
  - Video
  - The `.py` files.
  - The `books.csv` file.
  - The test case design document and test report.
  - Finally add the screenshots of the running program, otherwise you will lose the marks.





