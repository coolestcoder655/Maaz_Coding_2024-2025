# 📚 Library Management System

A simple terminal-based Library Management System built with Python. This project allows users to view, add, borrow, and return books through a console interface, with a touch of color styling using `colorama`.

## 📁 Project Structure
```
Library_Management_System/
├── src/
│   ├── modules/
│   │   └── libraryClass.py # Contains the Library class with all core functionalities 
│   └── main.py # Entry point and user interface logic │
└── README.md # This file
```
## ✨ Features

- View all available books in the library
- Add new books with title and author
- Borrow books by title (marked unavailable while borrowed)
- Return borrowed books
- Colorful and user-friendly CLI experience
- Error handling for empty inputs and duplicate entries

## 🚀 How to Run

1. Make sure you have Python installed (version 3.7+ recommended).
2. Install required package:

```bash
pip install colorama
```

Run the program:
```bash
python src/main.py
```
Use Ctrl + C anytime to exit the kiosk.

## 🧠 How It Works
The main user interaction is handled in main.py.

The actual book management logic (finding, adding, borrowing, returning) is encapsulated in the Library class found in `src/modules/libraryClass.py`.

Books are stored as a dictionary where each key is a unique `ISBN` (or generated UUID for new books), and the value is a dictionary with `title`, `author`, `isAvailable`, and `borrower`.

## 🛠 Example
```
Welcome To The Public Library Kiosk.
------------------------------------

Choose What You Would Like To Do:
  1. View Available Books
  2. Add New Book
  3. Borrow Book
  4. Return Book <br>
    ⚠️ Ctrl + C to Exit At Any Time ⚠️
```
## 📌 Notes
Titles are case-insensitive when searching.

Duplicate book titles are not allowed.

The system uses a simple in-memory structure and does not persist data (yet!).

## 📄 License
This project is open-source and free to use. Add a license here if you'd like to make it official!