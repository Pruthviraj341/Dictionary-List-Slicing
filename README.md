# Dictionary-List-Slicing
Student Marks Lookup

This is a simple Python program that allows you to look up a student's marks using a dictionary.
The student's name is used as the key, and their marks are stored as the value.

📌 Features

Stores student names and their marks in a dictionary.

Takes user input for a student’s name.

Retrieves and displays the marks if the student exists.

Shows a message if the student is not found in the record.
# key = student name , values = marks
students_marks = {'rayan':'79','brayan':'85','jason':'67','john':'90','joshu':'88'}
name = input("Enter student's name: ")

# retrieves marks of the students
if name in students_marks:
     print(f"The student {name} has a mark of {students_marks[name]}")
else:
     print(f"The student {name} has no mark")
🚀 How to Run

Save the code in a Python file, for example:
student_marks.py
Open a terminal or command prompt.

Run the program with:
python student_marks.py
Enter a student’s name when prompted.

📝 Example Run
Enter student's name: john
The student john has a mark of 90
Enter student's name: alex
The student alex has no mark

List Operations in Python

This Python program demonstrates basic list operations such as slicing and reversing.

📌 Features

Creates a list of numbers from 1 to 10.

Prints the original list.

Displays the first five elements of the list using slicing.

Reverses the list and prints the result.
# step 1 : create a list of numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

# original list
print("Original list:", numbers)

# first five elements
print("First five elements: ", numbers[:5])

# reverse the list
numbers.reverse()
print("Reversed list:", numbers)
🚀 How to Run

Save the code in a Python file, e.g.
list_operations.py
Open a terminal or command prompt.

Run the program with:
python list_operations.py
📝 Example Run
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
First five elements:  [1, 2, 3, 4, 5]
Reversed list: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
