students={ 
    "john":85,
    "Alice": 92,
    "Mike": 78
}
name=input("Enter new student name: ")
grade=int(input("Enter grade: "))
students[name]=grade

name= input("Enter student name to update: ")
if name in students:
    grade = int(input("Enter new grade:"))
    students[name]= grade
else:
    print("student not found.")

print("\nStudent Grades: ")
# for name, grades in students.items():
#     print(name, ":", grades)
print(students)