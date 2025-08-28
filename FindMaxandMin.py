# This program is about to find the maximum and minimum from entered elements

elements = int(input("Enter number of elements from which you want to find Maximum and Minimum: "))
print("Enter",elements,"Elements")

max = float('-inf')
min = float('inf')
i = 0

while i < elements:
    i = i +1
    x = int(input(""))
    if x > max:
        x =max
    if x < min:
       x = min
print("Max element: ", max)
print("Min element: ", min)