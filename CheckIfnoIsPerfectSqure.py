#This program is about to check if the number is perfect square or not

n = int(input("Enter a number: "))
i = 1
is_perfect_square = False

while i*i <= n:
    if i*i == n:
        is_perfect_square = True
        break
    i += 1

if is_perfect_square:
    print(f"{n} is perfect square")
else:
    print(f"{n} is not a perfect square")