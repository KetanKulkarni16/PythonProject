#This program is about to print the first five multiplies of 3

n = int(input("Enter a number: "))
count = 1

while count <= 5:
    print(n, end=" ")
    n += 3
    count +=1