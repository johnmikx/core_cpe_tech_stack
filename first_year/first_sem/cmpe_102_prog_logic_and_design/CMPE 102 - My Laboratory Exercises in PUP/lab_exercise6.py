# Program: Even Number Average Program (Laboratory Exercise 6)
# Author: John Mike P. Asuncion
# Date: January 7, 2024

import math

def main():
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
            print("")

        # List all inputted numbers
        print(f"All numbers entered: {all_numbers}")

        # Ask the user if they want to try again
        try_again = input("Would you like to try again? (yes[y]/no[n]): ").strip().lower()
        if try_again != 'y':
            print("Thank you for using the program. Goodbye!")
            break

if __name__ == "__main__":
    main()