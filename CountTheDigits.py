#This program is about to count the digits of the numbers

number = int(input("Enter the number: "))
c = 0
while number > 0:
     c = c + 1
     number = number // 10
     print(c)