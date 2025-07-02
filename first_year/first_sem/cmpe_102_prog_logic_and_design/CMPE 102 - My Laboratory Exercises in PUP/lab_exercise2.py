# Program: Weather Advisory Based on the Temperature Program
# Author: John Mike P. Asuncion
# Date: November 9, 2024

temperature = float(input("Enter the Temperature: "))

# If the condition is True, that means that the weather is severely cold.
if temperature < 0:
    print("It's freezing! Wear a heavy coat.")

# If the condition is True, that means that the weather is moderately cold.
elif 0 <= temperature <= 15:
    print("It's chilly! Wear a jacket.")

# If the condition is True, that means that the weather is mildy cold.
elif 16 <= temperature <= 25:
    print("It's cool! A sweater should be enough.")

# If all of the condition above is False, that means that the weather is hot.
else: 
    print("It's warm! Light clothing is recommended.")