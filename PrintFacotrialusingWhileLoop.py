#This program is about to print factorial using while loop

n = int(input("Enter the number : "))
fact =1
i = 1
while i <= n:
    fact = fact * i
    i = i+1
print("Factorial = ", fact)