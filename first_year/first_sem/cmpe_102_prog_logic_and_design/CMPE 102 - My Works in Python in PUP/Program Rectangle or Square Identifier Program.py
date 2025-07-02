# Program: Rectangle or Square Identifier
# Author: John Mike P. Asuncion
# Date: October 15, 2024

print("What is the width of a given quadrilateral?")
width = int(input())
print("What is the length of a given quadrilateral?")
length = int(input())
if width == length:
	print("The given quadrilateral is square.")
else:
	print("The given quadrilateral is rectangle.")