# ICE1: Review of Python

## **Introduction**
This tutorial covers fundamental Python concepts and provides a step-by-step guide to completing an assignment that analyzes movie budgets. You will learn about Python's data types, loops, conditionals, and file handling.

---

## **Part 1: Review of Python Concepts**

### **1. Python Data Types**
Python offers several data types for handling data:
- **int**: For integers (e.g., `10`, `-3`).
- **float**: For decimal numbers (e.g., `3.14`, `-1.5`).
- **str**: For text (e.g., `"Hello World"`).
- **bool**: For Boolean values (`True`, `False`).
- **list**: Mutable collection (e.g., `[1, 2, 3]`).
- **tuple**: Immutable collection (e.g., `(1, 2, 3)`).
- **dict**: Key-value pairs (e.g., `{"name": "Alice", "age": 25}`).

 
 #### **Examples**:
```python
# Integers and Floats
x = 10
y = 3.14

# Strings
greeting = "Hello, Python!"

# Boolean
is_active = True

# List
fruits = ["apple", "banana", "cherry"]

# Tuple
coordinates = (10, 20, 30)

# Dictionary
student = {"name": "Alice", "age": 25}
```

---

#### ** User Input and Display**: 

Python makes it easy to interact with users by taking inputs and displaying outputs.



##### **Taking Input**
- Use `input()` to take user input. It always returns a string.
- Convert input to other data types if needed (e.g., `int`, `float`).

##### **Code Example**
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
```



##### **Displaying Output**
- Use `print()` to display text or variables.
- Use **f-strings** or `.format()` for inline formatting.

###### **Code Example**
```python
print(f"Hello, {name}. You are {age} years old.")
```


##### **Expected Output**
```
Enter your name: Alice
Enter your age: 25
Hello, Alice. You are 25 years old.
```
---

#### **1.2 Mutable vs Immutable Types**
- **Mutable**: Can be changed (e.g., `list`, `dict`).
- **Immutable**: Cannot be changed (e.g., `tuple`, `str`).

##### **Examples**:
```python
# Mutable List
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']

# Immutable Tuple: Tuples are immutable to ensure data integrity and make them hashable (usable as dictionary keys or in sets).
coordinates = (10, 20, 30)  # Immutable Tuple
# Accessing elements works fine
print(coordinates[1])  # Output: 20

# Attempting to modify a tuple
coordinates[1] = 25  # TypeError: 'tuple' object does not support item assignment

# Immutable String: Strings in Python are immutable. Operations on strings return a new string rather than modifying the original.
greeting = "Hello"
new_greeting = greeting.replace("H", "J")

print(greeting)       # Output: Hello (original remains unchanged)
print(new_greeting)   # Output: Jello (a new string is created)


```


#### **1.3 Python Collections: Lists, Tuples, and Dictionaries**
##### **List Example**
```python
# Lists are mutable and can store mixed data types
movies = ["Interstellar", "Inception", "Titanic"]
movies.append("Avatar")
print(movies)  # ['Interstellar', 'Inception', 'Titanic', 'Avatar']
```
##### **Tuple Example**
```python
# Tuples are immutable
movie_details = ("Interstellar", "Christopher Nolan", 2014, 165000000)
print(movie_details)  # ('Interstellar', 'Christopher Nolan', 2014, 165000000)

```

##### **Dictionary Example**
```python
# Dictionaries store key-value pairs
movie = {"title": "Interstellar", "director": "Christopher Nolan", "year": 2014}
print(movie["title"])  # Interstellar
```
##### Differences Between List, Tuple, and Dictionary:

| Feature            | List                          | Tuple                         | Dictionary                     |
|--------------------|-------------------------------|-------------------------------|--------------------------------|
| **Definition**     | Ordered, mutable collection.  | Ordered, immutable collection.| Unordered, mutable collection of key-value pairs. |
| **Syntax**         | `[`   `]`                     | `(`   `)`                     | `{`   `}`                     |
| **Mutability**     | Mutable (modifiable).         | Immutable (cannot modify).    | Mutable (modifiable).         |
| **Indexing**       | Supports indexing.            | Supports indexing.            | Key-based access (not indexed). |
| **Duplicates**     | Allows duplicates.            | Allows duplicates.            | Keys must be unique; values can be duplicated. |
| **Usage**          | General-purpose collection (Dynamic collections where data changes frequently).   | Fixed collection of data (Fixed, unchanging collections to ensure data integrity).     | Mapping data via keys ( Key-value pairs for quick lookups or mappings).         |
| **Example**        | `[1, 2, 3]`                   | `(1, 2, 3)`                   | `{"a": 1, "b": 2}`            |
---
---
## **2. Loops**
Loops allow repetition of code.

#### **For Loop**:
```python
# Iterating over a list
movies = ["Inception", "Titanic", "Avatar"]
for movie in movies:
    print(movie)
```

#### **While Loop**:
```python
# Repeating until a condition is met
count = 0
while count < 3:
    print("Count:", count)
    count += 1
```
---
#### **2.1 Iterating Over a List**
Lists are ordered and mutable, allowing iteration over their elements.

##### **Code Example:**
```python
# List of movies
movies = ["Inception", "Titanic", "Avatar"]

# Iterating over elements
for movie in movies:
    print(movie)

# Iterating with index and value
for index, movie in enumerate(movies):
    print(f"Index {index}: {movie}")
```

##### **Output:**
```
Inception
Titanic
Avatar
Index 0: Inception
Index 1: Titanic
Index 2: Avatar
```

---

#### **2.2 Iterating Over a Tuple**
Tuples are ordered and immutable.

##### **Code Example:**
```python
# Tuple of movie details
movie_details = ("Inception", 2010, "Christopher Nolan")

# Iterating over elements
for detail in movie_details:
    print(detail)

# Iterating with index and value
for index, detail in enumerate(movie_details):
    print(f"Index {index}: {detail}")
```

##### **Output:**
```
Inception
2010
Christopher Nolan
Index 0: Inception
Index 1: 2010
Index 2: Christopher Nolan
```

---

#### **2.3 Iterating Over an Array**
Arrays are efficient, fixed-type collections, often used for numerical data.

##### **Code Example:**
```python
from array import array

# Array of budgets (in millions)
budgets = array("i", [165, 200, 356])

# Iterating over elements
for budget in budgets:
    print(budget)

# Iterating with index and value
for index, budget in enumerate(budgets):
    print(f"Index {index}: {budget}")
```

##### **Output:**
```
165
200
356
Index 0: 165
Index 1: 200
Index 2: 356
```

---

#### **2.4 Iterating Over a Dictionary**
Dictionaries store data as key-value pairs.

##### **Code Example:**
```python
# Dictionary of movie and budget
movie_budgets = {"Inception": 165, "Titanic": 200, "Avatar": 356}

# Iterating over keys
for movie in movie_budgets:
    print(movie)

# Iterating over keys and values
for movie, budget in movie_budgets.items():
    print(f"{movie}: ${budget}M")

# Iterating over keys with index
for index, movie in enumerate(movie_budgets):
    print(f"Index {index}: {movie} - ${movie_budgets[movie]}M")
```

##### **Output:**
```
Inception
Titanic
Avatar
Inception: $165M
Titanic: $200M
Avatar: $356M
Index 0: Inception - $165M
Index 1: Titanic - $200M
Index 2: Avatar - $356M
```

---

#### **2.5 Iterating Using While Loop**
While loops execute until a condition is met.

##### **Code Example:**
```python
# Iterating through a list using while loop
movies = ["Inception", "Titanic", "Avatar"]
index = 0

while index < len(movies):
    print(f"Movie at index {index}: {movies[index]}")
    index += 1
```

##### **Output:**
```
Movie at index 0: Inception
Movie at index 1: Titanic
Movie at index 2: Avatar
```
---


---


## **3. Conditionals**
Conditionals allow decision-making.

#### **Example**:
```python
# If-else Example
budget = 200000000
if budget > 150000000:
    print("High budget movie")
else:
    print("Low budget movie")
```

---
## **4. Important Libraries**
- `math`: For mathematical operations.
- `random`: For generating random numbers.
- `statistics`: For statistical calculations.
- `os`: For file and directory operations
---


## **5. File Handling**
Python allows reading from and writing to files.

#### **Example**:
```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Hello, World!
```

---

## **Part 2: Assignment: Movie Budget Analysis**

### **Objective**
1. Calculate the **average budget** of movies.
2. Identify movies with budgets **higher than the average**.
3. Print the **number of movies** above the average budget.
4. Allow users to **add movies** to the dataset.
5. Use `MovieList.txt` for input and save results in `Output.txt`.

---

### **Step 1: Prepare the Files**
- **MovieList.txt** (Input File):
```
Movie Name, Budget
Interstellar, 165000000
Inception, 160000000
Titanic, 200000000
Avengers: Endgame, 356000000
Frozen II, 150000000
```

- **Output.txt** (Output File): Will be generated by the program.

---

### **Step 2: Python Code**

#### **Starter Code**:
```python
# Author: Your Name
# Date: YYYY-MM-DD
# Description: Analyze movie budgets and save results to a file.

def calculate_average_budget(movies):
    """Calculate the average budget of all movies."""
    budgets = [budget for _, budget in movies]
    return sum(budgets) / len(budgets)

def find_high_budget_movies(movies, average_budget):
    """Find movies with budgets higher than the average."""
    return [(name, budget) for name, budget in movies if budget > average_budget]

def read_movies_from_file(file_name):
    """Read movies from a file."""
    movies = []
    with open(file_name, "r") as file:
        lines = file.readlines()[1:]  # Skip header
        for line in lines:
            name, budget = line.strip().split(", ")
            movies.append((name, int(budget)))
    return movies

def write_results_to_file(file_name, average_budget, high_budget_movies):
    """Write analysis results to a file."""
    with open(file_name, "w") as file:
        file.write(f"Average Budget: ${average_budget:,.2f}\n")
        file.write("Movies with Budgets Higher than Average:\n")
        for name, budget in high_budget_movies:
            file.write(f"{name}: ${budget:,}\n")


if __name__ == "__main__":
    # Read movies from file
    movies = read_movies_from_file("MovieList.txt")

    # Calculate average budget
    average_budget = calculate_average_budget(movies)

    # Find high-budget movies
    high_budget_movies = find_high_budget_movies(movies, average_budget)

    # Print results
    print(f"Average Budget: ${average_budget:,.2f}")
    print("Movies with Budgets Higher than Average:")
    for name, budget in high_budget_movies:
        print(f"  {name}: ${budget:,}")

    # Write results to output file
    write_results_to_file("Output.txt", average_budget, high_budget_movies)
    print("Results saved to 'Output.txt'.")
```

---

### **Step 3: Execution and Submission**
1. **Run the Program**:
   - Ensure `MovieList.txt` exists in the same directory as the Python file.
   - Execute the program and verify the output in the console and `Output.txt`.

2. **Submission Requirements**:
   - Provide screenshots of:
     - Console output (program execution).
     - Contents of `Output.txt`.
   - Submit your `.py` file and `MovieList.txt`.

---

## **3. Summary**
This tutorial covered Python basics and guided you through creating a movie budget analysis program. By practicing these concepts, you'll develop a strong foundation in Python programming.



