
student = {
    "Name": "Mayra",
    "Course": "IT",
    "Semester": 6
}

print("Student Details:")
print(student)

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Course:", student.get("Course"))

student.update({"CGPA": 8.2})
print("Updated Dictionary:", student)