#This program is about to find if candidate is eligible for work

age = int(input("Enter the age of a person: "))
if age < 18 or age >= 60:
    print('This person is not eligible for work: ')
else:
    print('This person is eligible for work')