# This program is about to print the armstrong number while loop

n = int(input("Enter a number: "))
temp = n
sum = 0
digits = len(str(n))

while temp > 0:
    digits = temp % 10
    sum += digits ** digits
    temp = temp // 10
if n == sum:
    print("Armstrong Number")
else:
    print("Not armstrong number")