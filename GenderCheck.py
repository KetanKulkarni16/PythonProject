#This program is about to check Gender of a person

print("Enter your personal details below: ")

name= input("Enter your name: ")
gender = input("Enter your Gender: ")
age = int(input("Enter your age: "))
if (gender == 'm' or gender == 'M'):
    print("You are Male")
else:
    print("You are Female")