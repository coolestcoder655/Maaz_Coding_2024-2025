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
capstone/
    ├── .venv/
    ├── src/
    │   ├── __pycache__/
    │   │   ├── classes.cpython-313.pyc
    │   │   ├── googleAuthHelper.cpython-313.pyc
    │   │   ├── googleAuthServer.cpython-313.pyc
    │   │   └── main.cpython-313.pyc
    │   ├── classes.py
    │   ├── examAccount.json
    │   ├── googleAuthHelper.py
    │   ├── googleAuthServer.py
    │   └── main.py
    ├── README.md
    └── requirements.txt
```

## ✨ Features

- **User Authentication**: Secure login system with Google OAuth and email/password authentication

- **Add A New Student**: Initialize a new student record

- **Remove A Student**: Remove a student when no longer needed

- **View All Exams**: View all exams that were previously entered

- **Add Additional Exams**: Add exams to a student that has been created

- **Edit/Update Exams**: Edit (update) an exam that has already been created

- **Summary**: See a summary of the student's progress, and recognize any anomalies or improvements

- **Real-time Updates**: The program automatically updates student grades on Firebase, allowing other users to see changes in real-time

## 🏦 Classes

### `Exam`

The `Exam` class represents an exam and holds information about itself.

#### Methods

- `__init__(self, subject: str, score: int, max_score: int = 100, exam_date: date = date.today())`: Initializes a new exam with a subject, score, maximum possible score (default 100), and exam date (default today).

### `Student`

The `Student` class represents a student and provides methods to perform various operations.

#### Methods

- `__init__(self, name: str, exams: list[Exam])`: Initializes a new student with a name and a list of exams.
- `addExam(self, toAdd: Exam)`: Add a new exam to the student's list of exams.

## 🚀 Usage

To use the test management system, create instances of the `Student` class and call methods to perform various operations.

> Before using the application, please ensure that you are referencing the [`examAccount.json`](src/examAccount.json) correctly. This can result in an **_error_** if ignored.

```python
from classes import Student, Exam
from datetime import date

# Create an exam
exam = Exam("Mathematics", 85, 100, date.today())

# Create a student with exams
student = Student("John Doe", [exam])

# Add another exam
student.addExam(Exam("Science", 92, 100))
```

## Dependencies

> This project requires several dependencies to function. Please ensure that you have these installed.

### Required Dependencies

- **Python 3.13+**
- **Tkinter** _(Comes pre-installed with Python)_
- **Firebase Admin SDK** _(Install via: `pip install firebase-admin`)_
- **Flask** _(Install via: `pip install flask`)_
- **Google Auth Libraries** _(Install via: `pip install google-auth google-auth-oauthlib google-auth-httplib2`)_
- **Requests** _(Install via: `pip install requests`)_

### Installation

Install all dependencies using pip:

```powershell
pip install firebase-admin flask google-auth google-auth-oauthlib google-auth-httplib2 requests
```

Or install using the requirements file:

```powershell
pip install -r requirements.txt
```

## 📝 Script Overview

The main script [`main.py`](src/main.py) initializes the Firebase backend and provides a graphical user interface for users to interact with the system. It includes authentication functionality and the main application interface.

The [`classes.py`](src/classes.py) contains the `Student` and `Exam` classes with their methods, which are used to perform various operations such as adding students, managing exams, and calculating grades.

The [`googleAuthHelper.py`](src/googleAuthHelper.py) provides Google OAuth authentication functionality using Flask to handle the authentication flow.

The [`googleAuthServer.py`](src/googleAuthServer.py) contains additional Google authentication utilities and server functions.

The `.json` file, [`examAccount.json`](src/examAccount.json), contains Firebase service account credentials that allow the application to interact with the Firebase backend during operation.

## 🛠️ How to Run

You can run the student test management system in these simple steps:

### Prerequisites

1. **Install Python 3.13+**: Ensure Python is installed on your system
2. **Install Dependencies**: Install all required packages using the command provided in the Dependencies section
3. **Firebase Setup**: Ensure your `examAccount.json` file is properly configured with valid Firebase credentials

### Running the Application

1. **Navigate to the Source Directory**

   Open PowerShell and change the directory to the `src` folder of the project. Replace `pathToTheFile` with the actual path to the `src` folder.

   ```powershell
   cd "pathToTheFile\src"
   ```

2. **Execute the Main Script**

   Run the following command to start the student test management system:

   ```powershell
   python main.py
   ```

### Alternative: Running with Complete Path

If you prefer not to navigate to the file's directory, you can run the Python script directly by providing its full path:

```powershell
python "C:\Users\YourUsername\path\to\your\file\src\main.py"
```

### Authentication

The application supports two authentication methods:

- **Email/Password**: Standard authentication using Firebase Auth
- **Google OAuth**: Login using your Google account

## 🚧 Coming Features

This application will (**_eventually_**) support filtering based on UUID for Firebase, to ensure that a student does not see their fellow students' grades.
