#This program is about to print the smallest digit

num = int(input("Enter the digit: "))
smallest_digit = 9 #initilize with largest possible digit
temp_num = num

if num == 0:
    smallest_digit = 0
else:
    while temp_num > 0:
        digit = temp_num % 10 # Get the last digit
        if digit < smallest_digit:
            smallest_digit = digit
        temp_num //= 10

print(f"The smallest digit in {num} is: {smallest_digit}")