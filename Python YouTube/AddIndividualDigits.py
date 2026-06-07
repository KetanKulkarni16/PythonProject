# This program is about to print the individual digits

n = int(input("Enter a number: "))
add = 0

while n > 0:
    r = n % 10
    add = add + r
    n = n // 10
print(add)