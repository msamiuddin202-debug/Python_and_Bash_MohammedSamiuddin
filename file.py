file = open("students.txt", "w")

file.write("Student Grades\n")
file.write("John: 85\n")
file.write("Alice: 92\n")
file.write("Mike: 78\n")

file.close()

print("Content written to file successfully.")