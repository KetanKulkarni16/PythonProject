# This program is about to find the last digit of the number

number = int(input("Enter the number"))

while number > 0:
    r = number % 10
    number = number // 10

print(r)
