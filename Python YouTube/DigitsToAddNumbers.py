#This program is to add digits of the number using type conversion

number=input("Enter a two digit number: ")  #Input any two digit number
first_digit=number[0]       #Separate first digit using index an array concept
second_digit=number[1]      #separate second digit using index of an array concept

print(int(first_digit) + int(second_digit)) #Add this two digits and type convert it to an int