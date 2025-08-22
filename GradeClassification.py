#This program is about the grade classification of the student

marks = int(input("Enter Marks: "))

if marks >= 90:
    print("A")

elif marks <90 and marks >= 75:
    print("B")

elif marks < 75 and marks >= 40:
    print("C")

elif marks < 40 and marks >=35:
    print("D")

else:
    print("Fail")