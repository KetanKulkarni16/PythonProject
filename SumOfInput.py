# This Program is about to find the sum of all the N numbers

n = int(input("Enter N number upto: "))
i = 0
sum = 0

print("Enter",n,"Numbers")

while i < n:
    i = i+1
    x= int(input())
    sum+=x
print("The sum of given numbers is: ",sum)