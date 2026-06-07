# This program is about to find the Factorial of the number
from math import factorial

number = int(input("Enter the number you want a factorial of: "))
factorial = 1

for i in range(1, number +1):
    factorial = factorial * i
print("Factorial of the",number, "is : ", factorial)