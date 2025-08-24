# This program is about to print the sum of the number of the digits

number = int(input("Enter the number: "))
sum = 0

while number > 0:
    r = number % 10
    sum = sum + r
    number = number // 10
print("The sum of digit is: ", sum)