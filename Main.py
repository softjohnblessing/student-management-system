import json
import os

# File to store student data
FILE_NAME = "students.json"

# Load existing students
def load_students():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save students
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# Add a student
def add_student():
    students = load_students()
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    student_id = input("Enter student ID: ")
    department = input("Enter department: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "department": department
    }

    students.append(student)
    save_students(students)
    print(f"\n Student {name} added successfully!\n")

# View all students
def view_students():
    students = load_students()
    if not students:
        print("\nNo students found.\n")
        return
    print("\n STUDENT LIST:")
    for student in students:
        print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Department: {student['department']}")
    print()

# Update a student record
def update_student():
    students = load_students()
    student_id = input("Enter the Student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            print(f"\nEditing record for {student['name']}")
            student["name"] = input("Enter new name: ") or student["name"]
            student["age"] = input("Enter new age: ") or student["age"]
            student["department"] = input("Enter new department: ") or student["department"]
            save_students(students)
            print("\n Student record updated successfully!\n")
            return
    print("\n Student not found.\n")

# Delete a student record
def delete_student():
    students = load_students()
    student_id = input("Enter the Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print(f"\n Student {student['name']} deleted successfully!\n")
            return
    print("\n Student not found.\n")

# Search for a student
def search_student():
    students = load_students()
    keyword = input("Enter name or ID to search: ").lower()
    results = [s for s in students if keyword in s["name"].lower() or keyword in s["id"]]
    
    if results:
        print("\n Search Results:")
        for s in results:
            print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Department: {s['department']}")
    else:
        print("\n No matching student found.\n")
    print()

# Menu system
def menu():
    while True:
        print("\n====== STUDENT MANAGEMENT SYSTEM ======")
        print("1️ Add Student")
        print("2️ View Students")
        print("3️ Update Student")
        print("4️ Delete Student")
        print("5️ Search Student")
        print("6️ Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            print("\n Exiting program... Goodbye!\n")
            break
        else:
            print("\n Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    menu()
