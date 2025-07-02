# Program: Grade Calculator Program
# Author: John Mike P. Asuncion
# Date: November 16, 2024

# Directions: Create a program that will compute for the final grade (Lecture 60% + Lab 40%) of a student based on the given criteria.

# Function to compute weighted grade
def compute_grade(quiz, midterm_exam, project, assignment_seatwork, recitation):
    return (quiz * 0.25) + (midterm_exam * 0.35) + (project * 0.15) + (assignment_seatwork * 0.15) + (recitation * 0.10)

# Main Program
print("\tWelcome to the Grade Calculator!".expandtabs(20))

# Input Student Name
name = input("\nWhat is your name?: ")
print(f"Hello {name}!")

# Input Grades for Lecture
print("\n\tEnter your Lecture Grades".expandtabs(20))
lecture_quiz = float(input("Enter your Lecture Quiz: "))
lecture_midterm_exam = float(input("Enter your Lecture Midterm Exam: "))
lecture_project = float(input("Enter your Lecture Project: "))
lecture_assignment_seatwork = float(input("Enter your Lecture Assignment/Seatwork: "))
lecture_recitation = float(input("Enter your Lecture Recitation: "))

# Compute Lecture Grade
lecture_grade = compute_grade(lecture_quiz, lecture_midterm_exam, lecture_project, lecture_assignment_seatwork, lecture_recitation)

# Input Grades for Laboratory
print("\n\tEnter your Laboratory Grades".expandtabs(20))
laboratory_quiz = float(input("Enter your Laboratory Quiz: "))
laboratory_midterm_exam = float(input("Enter your Laboratory Midterm Exam: "))
laboratory_project = float(input("Enter your Laboratory Project: "))
laboratory_assignment_seatwork = float(input("Enter your Laboratory Assignment/Seatwork: "))
laboratory_recitation = float(input("Enter your Laboratory Recitation: "))

# Compute Laboratory Grade
laboratory_grade = compute_grade(laboratory_quiz, laboratory_midterm_exam, laboratory_project, laboratory_assignment_seatwork, laboratory_recitation)

# Compute Final Grade
final_grade = (lecture_grade * 0.60) + (laboratory_grade * 0.40)

# Determine Equivalent Grade and Status According to the Grading System
if 97 <= final_grade <= 100:
    equivalent = "1.00"
elif 94 <= final_grade < 97:
    equivalent = "1.25"
elif 91 <= final_grade < 94:
    equivalent = "1.50"
elif 88 <= final_grade < 91:
    equivalent = "1.75"
elif 85 <= final_grade < 88:
    equivalent = "2.00"
elif 82 <= final_grade < 85:
    equivalent = "2.25"
elif 79 <= final_grade < 82:
    equivalent = "2.50"
elif 76 <= final_grade < 79:
    equivalent = "2.75"
elif 75 <= final_grade < 76:
    equivalent = "3.00"
else:
    equivalent = "5.00"

if float(equivalent) <= 3.00:
    status = "Passed"
else:
    status = "Failed"

# Display Results
print("\n\tResults".expandtabs(20))
print(f"Your Computed Grade for Lecture is {lecture_grade:.2f}.")
print(f"Your Computed Grade for Laboratory is {laboratory_grade:.2f}")
print(f"Your Final Grade is{final_grade: .2f} which is equivalent to {equivalent}. You {status}!")