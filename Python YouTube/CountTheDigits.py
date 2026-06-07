#This program is about to count the digits of the numbers

number = int(input("Enter the number: "))
i = 0
while number > 0:
     i = i + 1
     number = number // 10
print('Print no of digits', i)