# Program: Linear Search Algorithm Program
# Author: John Mike P. Asuncion
# Date: October 15, 2024

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i + 1
    return -1
    
arr = [1, 20, 30, 40]
target = 40
result = linear_search(arr, target)

if result != -1:
    print("Target found at index " + str(result) + ".")
else:
    print("Target not found in array.")