# This program is about to find the maximum element using while loop


n = int(input("From how many elements you want to find the maximum number: "))
print("Enter",n,"Elements:")
max = 0
i = 0

while i < n:
    i = i+1
    x=int(input(""))
    if x > max:
        max =x

print("Max element is: ", max)