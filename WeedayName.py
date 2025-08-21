#This program is about to print the Name of the day when day number is provided

print("Enter the day Number: ")

day= int(input("Day: "))


if day <=0 and day >=7 or day == 0:
    print("Invalid day of the week")

else:
        if day == 1:
            print("Monday")
        elif day==2:
            print("Tuesday")
        elif day==3:
            print("Wednesday")
        elif day==4:
            print("Thursday")
        elif day==5:
            print("Friday")
        elif day==6:
            print("Saturday")
        else:
            print("Sunday")
