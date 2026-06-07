# This program is about to print the sum of all the natural numbers using for loop

number = int(input("Enter the number: "))

sum = 0

for i in range (1,number+1):
    sum = sum + i
print("Sum of natural number: ", sum)