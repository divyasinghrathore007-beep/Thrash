# Student Management System 

import json

students = {}   # {id: {"name": ..., "marks": ..., "grade": ...}}


def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"


def load_data():
    global students
    try:
        f = open("students.json", "r")
        students = json.load(f)
        f.close()
    except FileNotFoundError:
        students = {}


def save_data():
    f = open("students.json", "w")
    json.dump(students, f)
    f.close()
    print("Data saved!")


def add_student():
    sid = input("Enter ID: ")
    if sid in students:
        print("ID already exists!")
        return
    name = input("Enter name: ")
    try:
        marks = float(input("Enter marks: "))
    except ValueError:
        print("Marks must be a number!")
        return
    students[sid] = {"name": name, "marks": marks, "grade": get_grade(marks)}
    print("Student added!")


def show_all():
    if len(students) == 0:
        print("No students found.")
        return
    for sid in students:
        s = students[sid]
        print(sid, "|", s["name"], "|", s["marks"], "|", s["grade"])


def search_student():
    sid = input("Enter ID to search: ")
    if sid in students:
        s = students[sid]
        print("Name:", s["name"], "| Marks:", s["marks"], "| Grade:", s["grade"])
    else:
        print("Student not found.")


def update_student():
    sid = input("Enter ID to update: ")
    if sid in students:
        students[sid]["name"] = input("Enter new name: ")
        try:
            marks = float(input("Enter new marks: "))
            students[sid]["marks"] = marks
            students[sid]["grade"] = get_grade(marks)
            print("Updated!")
        except ValueError:
            print("Marks must be a number!")
    else:
        print("Student not found.")


def delete_student():
    sid = input("Enter ID to delete: ")
    if sid in students:
        del students[sid]
        print("Deleted!")
    else:
        print("Student not found.")


def show_stats():
    if len(students) == 0:
        print("No data.")
        return
    marks_list = []
    for sid in students:
        marks_list.append(students[sid]["marks"])
    print("Average:", sum(marks_list) / len(marks_list))
    print("Highest:", max(marks_list))
    print("Lowest :", min(marks_list))


load_data()

while True:
    print("\n1. Add  2. View All  3. Search  4. Update  5. Delete  6. Stats  7. Save  8. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_all()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        show_stats()
    elif choice == "7":
        save_data()
    elif choice == "8":
        save_data()
        print("Bye!")
        break
    else:
        print("Invalid choice!")
