#This program is about to print the Fibonacchi series using for loop

n = int(input("Enter the number for Fibonacchi Series: "))
a = 0
b = 1

for i in range(0, n):
    c = a + b
    a = b
    b = c
print(a)