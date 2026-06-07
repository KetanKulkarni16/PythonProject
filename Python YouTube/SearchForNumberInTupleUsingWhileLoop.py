#This program is about to search and print the number in tuple using while loop also known as Traversing

nums = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter the square of the numbers between 2 to 10: "))
idx = 0

while idx < len(nums):
    if(nums[idx] == x):
        print("FOUND ! at index: ", idx)
    idx = idx + 1