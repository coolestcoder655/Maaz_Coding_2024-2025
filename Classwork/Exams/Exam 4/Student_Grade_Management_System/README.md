# Student Grade Management System

## Overview
The Student Grade Management System is a Python application that allows users to manage student grades. Users can add, remove, and update grades for different courses, as well as calculate the average grade for a student.

## Features
- Add a grade for a course
- Remove a grade for a course
- Update a grade for a course
- Calculate the average grade for a student
- Switch between different students

## Usage
1. Run the `main.py` script.
2. Enter the student's last and first name separated by a comma and space (e.g., "Doe, John").
3. Choose an option from the menu:
   - 1: Add a grade
   - 2: Remove a grade
   - 3: Modify a grade
   - 4: Calculate average
   - 5: Change student

## Example
```python
# Example of creating students and managing grades
myStudent1 = Student("Maaz", "Khokhar", {"english": 50, "spanish": 60})
myStudent2 = Student("John", "Doe", {"math": 75, "science": 85})
myStudent3 = Student("Jane", "Smith", {"history": 90, "art": 95})
myStudent4 = Student("Alice", "Johnson", {"biology": 80, "chemistry": 70})
myStudent5 = Student("Bob", "Brown", {"physics": 65, "geography": 55})
```

## Dependencies
- colorama

Install the dependencies using:
```bash
pip install colorama
```