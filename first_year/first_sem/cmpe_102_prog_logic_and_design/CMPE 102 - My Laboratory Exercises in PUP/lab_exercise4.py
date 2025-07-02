# Program: Asterisk Pyramid Program
# Author: John Mike P. Asuncion
# Date: December 14, 2024

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