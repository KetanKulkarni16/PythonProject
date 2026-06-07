#This program is about to start a count down

start_number = int(input("Enter a number to start a countdown : "))
current_number = start_number

while current_number > 0:
    print(current_number)
    current_number -= 1
print("Blast Off")