# Menu-Driven Student Information System
students = {}
def add_student():
    roll = input("Enter Roll No: ")
    students[roll] = {"Name": input("Enter Name: "), "Department": input("Enter Department: ")}
    print("Student added successfully.")

def view_students():
    if not students:
        return print("No student records found.")
    print("\n--- Student Records ---")
    for roll, d in students.items():
        print("Roll No:", roll, "| Name:", d["Name"], "| Department:", d["Department"])

def search_student():
    print(students.get(input("Enter Roll No to search: "), "Student not found."))

def delete_student():
    found = students.pop(input("Enter Roll No to delete: "), None)
    print("Student deleted successfully." if found else "Student not found.")

actions = {"1": add_student, "2": view_students, "3": search_student, "4": delete_student}

while True:
    print("\n1. Add Student\n2. View Students\n3. Search Student\n4. Delete Student\n5. Exit")
    choice = input("Enter your choice: ")
    if choice == "5":
        print("Exiting...")
        break
    actions.get(choice, lambda: print("Invalid choice."))()