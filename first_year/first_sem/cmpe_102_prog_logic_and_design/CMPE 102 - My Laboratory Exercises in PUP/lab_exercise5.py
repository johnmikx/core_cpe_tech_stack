# Program: Breakdown Program
# Author: John Mike P. Asuncion
# Date: December 14, 2024

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
    count_005 = 0
    count_001 = 0
    if amount>0:
        while amount >= 1000:
            amount = amount - 1000
            count_1000 += 1
        print("Value of 1000=", count_1000)
        while amount >= 500:
            amount = amount - 500
            count_500 += 1
        print("Value of 500=", count_500)
        while amount >= 200:
            amount = amount - 200
            count_200 += 1
        print("Value of 200=", count_200)
        while amount >= 100:
            amount = amount - 100
            count_100 += 1
        print("Value of 100=", count_100)
        while amount >= 50:
            amount = amount - 50
            count_50 += 1
        print("Value of 50=", count_50)
        while amount >= 20:
            amount = amount - 20
            count_20 += 1
        print("Value of 20=", count_20)
        while amount >= 10:
            amount = amount - 10
            count_10 += 1
        print("Value of 10=", count_10)
        while amount >= 5:
            amount = amount - 5
            count_5 += 1
        print("Value of 5=", count_5)
        while amount >= 1:
            amount = amount - 1
            count_1 += 1
        print("Value of 1=", count_1)
        while amount >= 0.25:
            amount = amount - 0.25
            count_025 += 1
        print("Value of 0.25=", count_025)
        while amount >= 0.05:
            amount = amount - 0.05
            count_005 += 1
        print("Value of 0.05=", count_005)
        count_001 = round(amount * 100)
        amount = 0
        print("Value of 0.01=", count_001)
    else:
        print("Invalid input, Please enter a Positive Number.")
    print(amount1)
    again = str(input("Continue, Yes(Y) or No(N)?"))