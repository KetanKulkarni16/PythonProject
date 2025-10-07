#This program is about to print the sum of the numbers between 1 to n

n = int(input("Enter the number: "))
i = 1
total = 0
while i <= n:
    total = total + i
    i = i+1
print("Sum = ", total)