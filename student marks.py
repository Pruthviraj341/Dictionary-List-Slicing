#   key = student name , values = marks
students_marks = {'rayan':'79','brayan':'85','jason':'67','john':'90','joshu':'88'}
name = input("Enter students name: ")

# retrives marks of the students
if name in students_marks:
     print(f"The student {name} has a mark of {students_marks[name]}")
else:
 print(f"The student {name} has no mark")