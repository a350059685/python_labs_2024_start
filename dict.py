import json

with open('students.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

students = data['students']

for student in students:
    print(f"{student['name']}")
    print(f"Age: {student['age']}")
    print(f"ID: {student['id']}")
    print(f"Grades: {student['grades']}")
    print()

for studnet in students:
    grades = student['grades']
    average_grade = sum(grades.values()) / len(grades)
    print(f"{student['name']}'s average grade: {average_grade}")