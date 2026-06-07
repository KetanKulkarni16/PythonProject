# This program is about to print the reverse number with dynamic method

n = int(input("Enter a number: "))
add = 0
while n > 0:
    r = n % 10
    add = add * 10 + r
    n = n // 10
print("Reverse = ", add)

#THis is check

print(add * 2)