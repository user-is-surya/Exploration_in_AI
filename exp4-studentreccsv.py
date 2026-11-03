# Student Record Management with List, Tuple, Dictionary and CSV
import csv

fields = ["RollNo", "Name", "Department", "Mark"]
rows = [("101", "Anitha", "CSE", 86), ("102", "Bala", "CSE", 91), ("103", "Chitra", "ECE", 78)]
students = [dict(zip(fields, r)) for r in rows]  # list of dictionaries

course = ("Python", 4)  # tuple: fixed course details
print("Course Tuple:", course)

with open("students.txt", "w") as f:
    f.writelines(f"{s}\n" for s in students)

with open("students.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(students)

print("\n--- Records from CSV ---")
with open("students.csv") as f:
    for row in csv.DictReader(f):
        print(*row.values())