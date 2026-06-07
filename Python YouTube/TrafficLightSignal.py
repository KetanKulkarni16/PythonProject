# This program is about the traffic light system

signal = str(input("Enter Signal Color: "))

if signal == 'red':
        print("Stop")
elif signal == 'yellow':
        print("Wait")
elif signal =='green':
    print("Go")
else:
    print("Invalid color enter again")