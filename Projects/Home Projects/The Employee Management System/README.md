
# Employee Management System

This project is an Employee Management System (EMS) that reads employee data from a text file and generates employee objects. It provides a simple interface to manage employee information.


## Project File Outline
```
employee-management-system
├── src
│   ├── main.py          # Entry point of the application
│   ├── employee.py      # Defines the Employee class
│   ├── state.py         # Shows The Program Which State The Code Is Currently In
│   ├── floormart.py     # Defines the Floormart Class
│   └── utils.py         # Utility functions for reading employee data
├── employees.txt        # Contains employee data
└── README.md            # Documentation for the project
```

## Files Overview

- **src/main.py**: This file is the entry point of the application. It reads the `employees.txt` file, processes the data, and creates employee objects based on the information provided.

- **src/employee.py**: This file defines the `Employee` class, the `Developer` class, the `Manager` class, the `CEO` class, the `Security Guard` class, the `Janitor` class, and the `ITSupport`. The classes has properties such as `name`, `phone_number`, and `salary`, and methods for initializing their respective objects and displaying the worker's details.

- **src/ultilites.py**: This file contains utility functions for reading the `employees.txt` file and parsing the employee data into a format suitable for creating `Employee` objects. It also includes the `listItems` function, which allows for easy enumeration and display of list elements across different modules.

- **employees.txt**: This file contains the employee data in a specific format, with each line representing an employee's name, phone number, and pay. 

## How to Run the Application

1. Ensure you have Python installed on your machine.
2. Download the project files.
3. Navigate to the `src` directory.
4. Run the application using the command:
   ```
   python main.py
   ```

## Functionality

The application reads employee data from `employees.txt`, creates `Employee` objects, and allows for further processing or management of employee information.