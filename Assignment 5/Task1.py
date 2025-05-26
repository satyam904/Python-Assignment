student_marks = {
    "Alice" : 85,
    "Bob" : 72,
    "Charlie" : 99,
    "David" : 58,
}

studemt_name = input("Enter a student name : ")

if studemt_name in student_marks :
    print(f"{studemt_name} marks : {student_marks[studemt_name]}")

else :
    print("Student not found")