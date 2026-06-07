#This program is about to check temperature

temp = float(input("Enter the Temperature: "))

if temp == 25:
    print("Normal")
else:
    if temp < 25:
            print("Cold")
    else:
            print("Hot")