# This program is about to print the reverse a number from user input

n = int(input("Enter a number: "))

while n > 0:
    r = n % 10
    print(r, end='')  #
    n = n // 10
