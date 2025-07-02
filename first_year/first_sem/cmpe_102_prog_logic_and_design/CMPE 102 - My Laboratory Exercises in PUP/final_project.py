# Main Menu for Laboratory Exercises
# Author: John Mike Asuncion
# Date: January 24, 2025

while True:
    print("\nMain Menu")
    print("1. Escape Sequence Program (Lab Exercise 1)")
    print("2. Weather Advisory Program (Lab Exercise 2)")
    print("3. Grade Calculator Program (Lab Exercise 3)")
    print("4. Asterisk Pyramid Program (Lab Exercise 4)")
    print("5. Breakdown Program (Lab Exercise 5)")
    print("6. Even Number Average Program (Lab Exercise 6)")
    print("7. Exit")

    try:
        choice = int(input("\nEnter your choice (1-7): "))
        if choice == 1:
            # Lab Exercise 1: Escape Sequence Program
            print("\nRunning Escape Sequence Program...")
            # Code for Lab Exercise 1
            string1 = "\tI"
            new_strings1 = string1.expandtabs(23)
            print(new_strings1)
            
            string2 = "\tThink"
            new_strings2 = string2.expandtabs(21)
            print(new_strings2)

            string3 = "\tThat I shall"
            new_strings3 = string3.expandtabs(17)
            print(new_strings3)

            string4 = "\tNever see a poem"
            new_strings4 = string4.expandtabs(15)
            print(new_strings4)

            string5 = "\tAs lovely as a tree,"
            new_strings5 = string5.expandtabs(13)
            print(new_strings5)

            string6 = "\tA tree whose hungry mouth"
            new_strings6 = string6.expandtabs(11)
            print(new_strings6)

            string7 = "\tIs pressed against the earth's"
            new_strings7 = string7.expandtabs(8)
            print(new_strings7)

            string8 = "\tSweet flowing breast, a tree that"
            new_strings8 = string8.expandtabs(7)
            print(new_strings8)

            string9 = "\tLooks at God all day, and lifts it's"
            new_strings9 = string9.expandtabs(6)
            print(new_strings9)

            string10 = "\tLeafy arms to pray. A tree that may in"
            new_strings10 = string10.expandtabs(5)
            print(new_strings10)

            string11 = "\tSummer wear, a nest of robin in her hair;"
            new_strings11 = string11.expandtabs(4)
            print(new_strings11)

            string12 = "\tUpon whose bosom snow has lain; who intimately"
            new_strings12 = string12.expandtabs(1)
            print(new_strings12)

            string13 = "\tLives with rain."
            new_strings13 = string13.expandtabs(16)
            print(new_strings13)

            string14 = "\tPoems are made by"
            new_strings14 = string14.expandtabs(15)
            print(new_strings14)

            string15 = "\tFools like Me"
            new_strings15 = string15.expandtabs(17)
            print(new_strings15)

            string16 = "\tBut"
            new_strings16 = string16.expandtabs(22)
            print(new_strings16)

            string17 = "\tOnly"
            new_strings17 = string17.expandtabs(21)
            print(new_strings17)

            string18 = "\tGod"
            new_strings18 = string18.expandtabs(22)
            print(new_strings18)

            string19 = "\tCan"
            new_strings19 = string19.expandtabs(22)
            print(new_strings19)

            string20 = "\tMake"
            new_strings20 = string20.expandtabs(21)
            print(new_strings20)

            string21 = "\tA"
            new_strings21 = string21.expandtabs(23)
            print(new_strings21)

            string22 = "\tTree"
            new_strings22 = string22.expandtabs(21)
            print(new_strings22)

            string23 = "\tJOYCE KILMER"
            new_strings23 = string23.expandtabs(17)
            print(new_strings23)

        elif choice == 2:
            # Lab Exercise 2: Weather Advisory Program
            print("\nRunning Weather Advisory Program...")
            temperature = float(input("Enter the Temperature: "))
            if temperature < 0:
                print("It's freezing! Wear a heavy coat.")
            elif 0 <= temperature <= 15:
                print("It's chilly! Wear a jacket.")
            elif 16 <= temperature <= 25:
                print("It's cool! A sweater should be enough.")
            else:
                print("It's warm! Light clothing is recommended.")

        elif choice == 3:
            # Lab Exercise 3: Grade Calculator Program
            print("\nRunning Grade Calculator Program...")
            def compute_grade(quiz, midterm_exam, project, assignment_seatwork, recitation):
                return (quiz * 0.25) + (midterm_exam * 0.35) + (project * 0.15) + (assignment_seatwork * 0.15) + (recitation * 0.10)

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

            print("\tWelcome to the Grade Calculator!".expandtabs(20))
            name = input("\nWhat is your name?: ")
            print(f"Hello {name}!")

            print("\n\tEnter your Lecture Grades".expandtabs(20))
            lecture_quiz = get_valid_grade("Enter your Lecture Quiz: ")
            lecture_midterm_exam = get_valid_grade("Enter your Lecture Midterm Exam: ")
            lecture_project = get_valid_grade("Enter your Lecture Project: ")
            lecture_assignment_seatwork = get_valid_grade("Enter your Lecture Assignment/Seatwork: ")
            lecture_recitation = get_valid_grade("Enter your Lecture Recitation: ")

            lecture_grade = compute_grade(lecture_quiz, lecture_midterm_exam, lecture_project, lecture_assignment_seatwork, lecture_recitation)

            print("\n\tEnter your Laboratory Grades".expandtabs(20))
            laboratory_quiz = get_valid_grade("Enter your Laboratory Quiz: ")
            laboratory_midterm_exam = get_valid_grade("Enter your Laboratory Midterm Exam: ")
            laboratory_project = get_valid_grade("Enter your Laboratory Project: ")
            laboratory_assignment_seatwork = get_valid_grade("Enter your Laboratory Assignment/Seatwork: ")
            laboratory_recitation = get_valid_grade("Enter your Laboratory Recitation: ")

            laboratory_grade = compute_grade(laboratory_quiz, laboratory_midterm_exam, laboratory_project, laboratory_assignment_seatwork, laboratory_recitation)

            final_grade = (lecture_grade * 0.60) + (laboratory_grade * 0.40)

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

            if float(equivalent_grade) <= 3.00:
                status = "Passed"
            else:
                status = "Failed"

            print("\n\tResults".expandtabs(20))
            print(f"Your Computed Grade for Lecture is {lecture_grade:.2f}")
            print(f"Your Computed Grade for Laboratory is {laboratory_grade:.2f}")
            print(f"Your Final Grade is{final_grade: .2f} which is equivalent to {equivalent_grade}. You {status}!")

        elif choice == 4:
            # Lab Exercise 4: Asterisk Pyramid Program
            print("\nRunning Asterisk Pyramid Program...")
            num = 0
            while num != 4:
                num = int(input("Hello! Choose a number(1-4): "))
                if num == 1:
                    for i in range(5):
                        print("*" * (i + 1))
                    for n in range(4, 0, -1):
                        print("*" * (n))
                if num == 2:
                    for i in range(5):
                        print(" " * (5 - i) + "*" * (i + 1))
                    for n in range(4, 0, -1):
                        print(" " * (6 - n) + "*" * (n))
                if num == 3:
                    for i in range(4):
                        print("*" * (i + 1) + " " * (7 - 2 * i) + "*" * (i + 1))
                    print("*" * 9)
                    for n in range (4, 0, -1):
                        print("*" * (n) + " " * (9 - 2 * n) + "*" * (n))
            else:
                print("Exiting the Program... Bye!")

        elif choice == 5:
            # Lab Exercise 5: Breakdown Program
            print("\nRunning Breakdown Program...")
            print ("Hi!")
            again = "Y"
            while again== "Y":
                amount1=float(input("Enter an amount: "))
                amount=amount1
                count_1000 = 0
                count_500 = 0
                count_200 = 0
                count_100 = 0
                count_50 = 0
                count_20 = 0
                count_10 = 0
                count_5 = 0
                count_1 = 0
                count_025 = 0
                count_05 = 0
                count_01 = 0

                if amount >= 1000:
                    count_1000 = int(amount / 1000)
                    amount = amount - (count_1000 * 1000)

                if amount >= 500:
                    count_500 = int(amount / 500)
                    amount = amount - (count_500 * 500)

                if amount >= 200:
                    count_200 = int(amount / 200)
                    amount = amount - (count_200 * 200)

                if amount >= 100:
                    count_100 = int(amount / 100)
                    amount = amount - (count_100 * 100)

                if amount >= 50:
                    count_50 = int(amount / 50)
                    amount = amount - (count_50 * 50)

                if amount >= 20:
                    count_20 = int(amount / 20)
                    amount = amount - (count_20 * 20)

                if amount >= 10:
                    count_10 = int(amount / 10)
                    amount = amount - (count_10 * 10)

                if amount >= 5:
                    count_5 = int(amount / 5)
                    amount = amount - (count_5 * 5)

                if amount >= 1:
                    count_1 = int(amount / 1)
                    amount = amount - (count_1 * 1)

                if amount >= 0.25:
                    count_025 = int(amount / 0.25)
                    amount = amount - (count_025 * 0.25)

                if amount >= 0.05:
                    count_05 = int(amount / 0.05)
                    amount = amount - (count_05 * 0.05)

                if amount >= 0.01:
                    count_01 = int(amount / 0.01)
                    amount = amount - (count_01 * 0.01)

                print("Breakdown:")
                print(f"1000 Peso Bill: {count_1000}")
                print(f"500 Peso Bill: {count_500}")
                print(f"200 Peso Bill: {count_200}")
                print(f"100 Peso Bill: {count_100}")
                print(f"50 Peso Bill: {count_50}")
                print(f"20 Peso Bill: {count_20}")
                print(f"10 Peso Coin: {count_10}")
                print(f"5 Peso Coin: {count_5}")
                print(f"1 Peso Coin: {count_1}")
                print(f"25 Centavo Coin: {count_025}")
                print(f"5 Centavo Coin: {count_05}")
                print(f"1 Centavo Coin: {count_01}")

                again = input("\nDo you want to input another amount? (Y/N): ").upper()

        elif choice == 6:
            # Lab Exercise 6: Even Number Average Program
            print("\nRunning Even Number Average Program...")
            import math

            while True:
                # Ask the user for the number of inputs
                while True:
                    try:
                        num_count = int(input("How many numbers would you like to input? "))
                        if num_count > 0:
                            break
                        else: 
                            print("Invalid input. Please enter a positive whole number.")
                    except ValueError:
                        print("Invalid input. Please enter a whole number.")

                even_numbers = []  # List to store even numbers
                all_numbers = []   # List to store all inputted numbers
                count = 0  # Counter for the while loop

                while count < num_count:
                    while True:  # Loop until a valid number is entered
                        user_input = input(f"Enter number {count + 1}: ")
                        
                        # Clean the input to remove any invalid characters
                        cleaned_input = ''.join(char for char in user_input if char.isdigit() or char in ['-', '.'])
                        
                        # Check if the cleaned input is valid
                        if cleaned_input.count('-') > 1 or cleaned_input.count('.') > 1 or cleaned_input == '':
                            print("Invalid input. Please enter a valid number.")
                            continue  # Prompt for input again
                        
                        # Convert the cleaned input to a float
                        try:
                            number = float(cleaned_input)
                            break  # Exit the loop if conversion is successful
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                    
                    # Use absolute value to handle negatives
                    abs_number = abs(number)
                    
                    # Determine if the number is even or odd using ceil
                    if abs_number % 1 != 0:  # Check if the number is a decimal
                        ceil_number = math.ceil(abs_number)
                        all_numbers.append(ceil_number)  # Store the ceiling value in the list of all numbers
                        if ceil_number % 2 == 0:
                            even_numbers.append(ceil_number)  # Add to the list of even numbers if it's even
                    else:
                        all_numbers.append(number)  # Store the original number if it's an integer
                        if math.floor(abs_number) % 2 == 0:
                            even_numbers.append(abs_number)  # Add to the list of even numbers if it's even
                    
                    count += 1  # Increment the counter

                # Calculate the average of the even numbers
                if even_numbers:
                    average = sum(even_numbers) / len(even_numbers)
                    print(f"The even numbers entered are: {even_numbers}")
                    print(f"The average of the even numbers is: {average}")
                else:
                    print("The even numbers entered are: 0 \nThe average of even numbers is: 0")

                # List all inputted numbers
                print(f"All numbers entered: {all_numbers}")

                # Ask the user if they want to try again
                try_again = input("Would you like to try again? (yes[y]/no[n]): ").strip().lower()
                if try_again != 'y':
                    print("Thank you for using the program. Goodbye!")
                    break

        elif choice == 7:
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

    except ValueError:
      print("Invalid input. Please enter a valid number.")