#This program is about to count the digits in number

n = int(input("Enter the number: "))
count = 0
while n > 0:
    count = count+1
    n = n // 10
print("Number of digits: ", count)