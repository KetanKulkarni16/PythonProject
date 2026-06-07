# This program is about to generate prime numbers between 1 to 100

number = 1
count = 0

for i in range(1, number + 1):
    if number % i == 0:
        count += 1

if count == 2:
    print(number)
