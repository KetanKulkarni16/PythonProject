# Check the number is palindrome or not

number = int(input("Enter the number: "))
n = number
rev = 0

while number > 0:
    r = number % 10
    rev = rev * 10 + r
    number = number // 10

print("Reversed Number is: ", rev)
if n == rev:
    print("Its Palindrome")
else:
    print("Not Palindrome")



