# Program: Grade Calculator Program
# Author: John Mike P. Asuncion
# Date: November 16, 2024

# Function to compute weighted grade
def compute_grade(quiz, midterm_exam, project, assignment_seatwork, recitation):
    return (quiz * 0.25) + (midterm_exam * 0.35) + (project * 0.15) + (assignment_seatwork * 0.15) + (recitation * 0.10)

# Function to validate input
def get_valid_grade(prompt):
    while True:
        try:
            grade = float(input(prompt))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Invalid input. Please enter a grade between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main Program
print("\tWelcome to the Grade Calculator!".expandtabs(20))

# Input Student Name
name = input("\nWhat is your name?: ")
print(f"Hello {name}!")

# Input Grades for Lecture
print("\n\tEnter your Lecture Grades".expandtabs(20))
lecture_quiz = get_valid_grade("Enter your Lecture Quiz: ")
lecture_midterm_exam = get_valid_grade("Enter your Lecture Midterm Exam: ")
lecture_project = get_valid_grade("Enter your Lecture Project: ")
lecture_assignment_seatwork = get_valid_grade("Enter your Lecture Assignment/Seatwork: ")
lecture_recitation = get_valid_grade("Enter your Lecture Recitation: ")

# Compute Lecture Grade
lecture_grade = compute_grade(lecture_quiz, lecture_midterm_exam, lecture_project, lecture_assignment_seatwork, lecture_recitation)

# Input Grades for Laboratory
print("\n\tEnter your Laboratory Grades".expandtabs(20))
laboratory_quiz = get_valid_grade("Enter your Laboratory Quiz: ")
laboratory_midterm_exam = get_valid_grade("Enter your Laboratory Midterm Exam: ")
laboratory_project = get_valid_grade("Enter your Laboratory Project: ")
laboratory_assignment_seatwork = get_valid_grade("Enter your Laboratory Assignment/Seatwork: ")
laboratory_recitation = get_valid_grade("Enter your Laboratory Recitation: ")

# Compute Laboratory Grade
laboratory_grade = compute_grade(laboratory_quiz, laboratory_midterm_exam, laboratory_project, laboratory_assignment_seatwork, laboratory_recitation)

# Compute Final Grade
final_grade = (lecture_grade * 0.60) + (laboratory_grade * 0.40)

# Determine Equivalent Grade and Status According to the Grading System
if final_grade >= 96.50:
    equivalent_grade = 1.00
elif final_grade >= 93.50:
    equivalent_grade = 1.25
elif final_grade >= 90.50:
    equivalent_grade = 1.50
elif final_grade >= 87.50:
    equivalent_grade = 1.75   
elif final_grade >= 84.50:
    equivalent_grade = 2.00
elif final_grade >= 81.50:
    equivalent_grade = 2.25
elif final_grade >= 78.50:
    equivalent_grade = 2.50
elif final_grade >= 75.50:
    equivalent_grade = 2.75
elif final_grade >= 74.50:
    equivalent_grade = 3.00
else:
    equivalent_grade = 5.00

# Determine Status
if float(equivalent_grade) <= 3.00:
    status = "Passed"
else:
    status = "Failed"

# Display Results
print("\n\tResults".expandtabs(20))
print(f"Your Computed Grade for Lecture is {lecture_grade:.2f}")
print(f"Your Computed Grade for Laboratory is {laboratory_grade:.2f}")
print(f"Your Final Grade is{final_grade: .2f} which is equivalent to {equivalent_grade}. You {status}!")