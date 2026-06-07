#This program is about to print the palindrome number


n = int(input("Enter the number: "))
add =0
call = n
while n > 0:
    r = n % 10
    add = add * 10 + r
    n = n // 10

if add == call:
    print("The number is palindrome")
else:
    print("Not palindrome")