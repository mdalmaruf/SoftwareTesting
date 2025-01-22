# Python Class Tutorial: A Beginner-Friendly Guide

## Introduction

A class in Python is a blueprint for creating objects. It allows us to group related attributes (data) and methods (functions) together, making the code more structured and reusable.

### Why Use Classes?
- **Encapsulation:** Grouping related data and functions.
- **Reusability:** Use code multiple times efficiently.
- **Modularity:** Breaking down large projects into manageable units.
- **Abstraction:** Hiding implementation details from users.
- **Inheritance:** Allowing code reuse across related objects.

---

![Components of a Class](images/class.png)
![Components of a Class](images/class0.png)


## Step 1: Creating a Basic Class

```python
class Student:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an instance of the class
student1 = Student("Alice", 20)

# Accessing attributes and calling methods
print(student1.name)  # Output: Alice
student1.display_info()  # Output: Name: Alice, Age: 20
```
---

## Step 2: Class vs Instance Attributes
- Instance Attributes: Unique to each object.
- Class Attributes: Shared across all objects.

```python
class Student:
    school_name = "Greenwood High"  # Class attribute

    def __init__(self, name):
        self.name = name  # Instance attribute

student1 = Student("Alice")
student2 = Student("Bob")

print(student1.school_name)  # Output: Greenwood High
Student.school_name = "Sunrise School"  # Changing class attribute

print(student2.school_name)  # Output: Sunrise School
```
---
## Step 3: Access Modifiers (Public, Protected, Private)
Python uses naming conventions for access control:

- Public Attributes: Accessible anywhere.
- Protected Attributes (_attribute): Should be accessed within subclasses.
- Private Attributes (__attribute): Cannot be accessed directly outside the class.

```python
class Student:
    def __init__(self, name, age):
        self.name = name  # Public
        self._age = age   # Protected
        self.__grade = 90  # Private

student1 = Student("Alice", 20)

print(student1.name)  # Works (public)
print(student1._age)  # Works (protected, but not recommended)
# print(student1.__grade)  # Raises AttributeError
```
---
## Step 4: Class Methods vs Instance Methods vs Static Methods
Python supports three types of methods:

- Instance Methods: Operate on an instance, need self.
- Class Methods: Operate on the class, use cls.
- Static Methods: Independent, no self or cls.
```python
class School:
    school_name = "Greenwood High"

    def __init__(self, student_name):
        self.student_name = student_name

    def instance_method(self):
        return f"Student: {self.student_name}"

    @classmethod
    def class_method(cls):
        return f"School: {cls.school_name}"

    @staticmethod
    def static_method():
        return "Welcome to the school"

s = School("Alice")
print(s.instance_method())  # Output: Student: Alice
print(School.class_method())  # Output: School: Greenwood High
print(School.static_method())  # Output: Welcome to the school

```
---
## Step 5: Inheritance (Code Reusability)
Inheritance allows a class to derive properties and methods from another class.
```python
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, I am {self.name}")

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def introduce(self):
        print(f"Hi, I am {self.name}, and my student ID is {self.student_id}")

student1 = Student("Bob", "S123")
student1.introduce()

```
---
## Step 6: Multiple Classes Working Together
Classes can work together through composition, where one class contains objects of another class.
```python
class Course:
    def __init__(self, course_name):
        self.course_name = course_name

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course  # Composition

    def display_info(self):
        print(f"Student: {self.name}, Course: {self.course.course_name}")

course1 = Course("Python Programming")
student1 = Student("Alice", course1)

student1.display_info()
```
---
## Step 7: Polymorphism (Same Method, Different Behavior)

```python
class Animal:
    def make_sound(self):
        print("Some sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

animals = [Dog(), Cat()]
for animal in animals:
    animal.make_sound()
```
---
## Step 8: Handling Errors Using Exceptions in Classes
```python
class Calculator:
    @staticmethod
    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

print(Calculator.divide(10, 0))  # Output: Error: Division by zero is not allowed.

```
---

## Step 9: Encapsulation (Hiding Data)
Encapsulation restricts direct access to attributes and methods and prevents accidental modification.
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# print(account.__balance)  # Raises AttributeError

```
---
## Conclusion
- Python classes help in organizing and structuring code.
- Key concepts include attributes, methods, inheritance, polymorphism, and encapsulation.
- Use classes to make code reusable and maintainable.
