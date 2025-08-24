#This program is about to reverse a number using while loop

number = int(input("Enter a number: "))
rev = 0

while number > 0:
    r = number % 10
    rev = rev * 10 + r
    number = number // 10
print("The reverse number is: ", rev)