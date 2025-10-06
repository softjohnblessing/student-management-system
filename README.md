# Student Management System

A simple **Python-based Student Management System (SMS)** that allows teachers or administrators to manage student records easily from the terminal.  
It supports adding, viewing, updating, deleting, and searching student data — with all records saved in a JSON file for persistence.

## Project Overview

This project was developed as part of a Python learning assignment to demonstrate:
Variables and Data Types  
Lists and Dictionaries  
Functions and Loops  
Conditionals and Error Handling  
File Handling (JSON)  
Git & GitHub version control  

## Features

Add new students (auto-generated ID)  
View all student records in a table-like format  
Update student information  
Delete students by ID  
Search for students by name or ID  
Save & load data automatically from `students.json`  
(Optional Bonus) Show simple statistics (e.g., total students, average age)

## Technologies Used

**Python 3**
**JSON** (for data storage)
**Git & GitHub** (for version control)

## Project Structure

student-management-system/
│
├── main.py          # Main program file
├── students.json    # JSON data file
└── README.md        # Documentation file


## How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/student-management-system.git
````

### 2️. Navigate into the Folder

```bash
cd student-management-system
```

### 3️. Run the Python Program

```bash
python main.py
```

> Make sure you have Python 3 installed. You can check by running:
>
> ```bash
> python --version
> ```


## Example Usage

**Menu:**

```
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Search Student
6. Exit
```

**Sample Data Stored in `students.json`:**

```json
[
    {
    "id": 1,
    "name": "Princess Blessing",
    "age": 20,
    "grade": "Year 10"
    },
    {
    "id": 2,
    "name": "Angel Smith",
    "age": 16,
    "grade": "Year 11"
    }
    ]

## Git Commands Used

```bash
git init
git add .
git commit -m "Initial commit - added main.py and students.json"
git remote add origin https://github.com/softjohnblessing/student-management-system
git branch -M main
git push -u origin main
```

##  Grading Criteria

| Criteria          | Description                        |
| ----------------- | ---------------------------------- |
| **Functionality** | Does it meet all requirements?     |
| **Code Quality**  | Clean, readable, and structured    |
| **Documentation** | Clear instructions in this README  |
| **Git Usage**     | Meaningful commits, organized repo |
| **Creativity**    | Bonus features or improvements     |

## Author

**Name:** Blessing John
**Project:** Student Management System
**Year:** 2025

## Acknowledgments

Special thanks to **CapacityBay** and my instructor **Favour Augustine** for their guidance and support in developing this project.