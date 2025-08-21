#This program is about to check if the given year is Leap year or Regular year
#This method is latest Method dependent on Gregorian Calendar which humans use today Julian calendar is outdated now to calculate
#Leap year in the programming 365.242 is exact extra day in every leap year
# if year % 400 == 0 comes from the Abdul bari Video Course on Udemy


print("Enter a year: ")
year = int(input("Year: "))

if year % 100 == 0:

    if year % 400 == 0:
        print("Its leap year")
    else:
        print("Not a leap year")

elif year % 4 == 0:
    print("Its leap year")
else:
    print("Its not leap year")