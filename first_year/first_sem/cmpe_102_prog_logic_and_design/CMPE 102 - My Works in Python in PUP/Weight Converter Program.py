# Program: Weight Converter Program
# Author: John Mike Asuncion
# Date: October 25, 2024

weight = int(input("Weight: "))
unit = input("(L)bs or (K)gs: ")

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos.")
else:
    converted = weight / 0.45
    print(f"You are {converted} pounds.")