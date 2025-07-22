# 📚 Student Test Management System

This program is designed to assist teachers in grading their student's tests.

## ⚛️ Tech Stack

| Feature  | Application          |
| -------- | -------------------- |
| Language | _Python v3.13.5_     |
| Database | _Firebase Firestore_ |
| Tkinter  | _GUI_                |

## 📁 File Structure

```plaintext
Capstone/
    ├── src/
    │   ├── __pycache__/
    │   │   ├── classes.cpython-313.pyc
    │   │   └── main.cpython-313.pyc
    │   ├── classes.py
    │   ├── main.py
    │   └── examAccount.json
    ├── Requirements.txt
    └── README.md
```

## ✨ Features

- **Add A New Student**: Initalize A New Student

- **Remove A Student**: Remove a Student When Created

- **View All Exams**: View All Exams That Were Previously Entered

- **Add Additonal Exams**: Add Exams To A Student That Has Been Created

- **Edit/Update Exams**: Edit (Update) an Exam That Has Already Been Created

- **Summary**: See a summary of the student's progress, and recognize any anomalies or improvements

- **Update Student's Grade Remotely**: The program automatically updates the student's grade on the remote end, allowing other users of this program to see the changes.

## 🏦 Classes

### `Exam`

The `Exam` class represents an exam and holds information about itself.

#### Methods

- `__init__(self, subject: str, score: int, max_score: int = 10`: Initializes a new exam with a subject, a score, and a max score the student could've achieved.

### `Student`

The `Student` class represents a student and provides methods to perform various operations.

#### Methods

- `__init__(self, name: str, exams: list[Exam])` Initializes a new student with a names, and a list of exams.
- `addExam(self, toAdd: Exam)`: Add a New Exam to the Student's List of Exams

## 🚀 Usage

To use the test management system, create instances of the `Student` class and call a method to perform various operations.

> Before using test cases, please ensure that you are refrencing the [`examAccount.json](src/examAccount.json) correctly. This can result in an **_error_** if ignored

```python
from classes import Student, Exam
```

## Dependencies

> This project uses a couple dependencies to function. Please ensure that you have these installed, or use the [`requirements.txt`](requirements.txt) file to install them.

- _**Tkinter**_ _(Comes Pre-Installed With Python)_
- _**Firebase Admin**_ _(Requires Installation via Python Package Manager)_

## 📝 Script Overview

The main script [`main.py`](src/main.py) initializes the firebase-backend and provides a graphical user interface for users to interact with the system.

The [`classes.py`](src/classes.py) contains the `Student` class and its methods and the `Exam` class, which are used to perform various operations such as adding a student, removing a student, view all exams, adding an exam, editting an exam, and creating a summary.

The `.json` file, [`examAccount.json`](src/examAccount.json), allows the [main](src/main.py) file to interact with the firebase backend during its operation.

## 🛠️ How to Run

You can run the bank management system in two simple steps:

1. **Navigate to the Source Directory**

   Open PowerShell and change the directory to the `src` folder of the project. Replace `pathToTheFile` with the actual path to the `src` folder.

   ```powershell
   cd "pathToTheFile"
   ```

2. **Execute the Main Script**

   Run the following command to start the bank management system:

   ```powershell
   python main.py
   ```

### Running a Python File Using the Complete Path

If you prefer not to navigate to the file's directory, you can run the Python script directly by providing its full path. Simply replace the path in the quotation marks with the actual location of your Python file.

```powershell
python "C:\Users\YourUsername\path\to\your\file\filename.py"
```
