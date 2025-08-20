#This program is about to find the exam results

math = int(input("Enter the marks for math: "))
phy = int(input("Enter the marks for physics: "))
chem = int(input("Enter the marks for chem: "))
if(math <=100 and phy<= 100 and chem <=100):
    if(math >=45 and phy >=45 and chem >=45 ):
        print("Congratulations You are passed Examinations: ")
    else:
        print("You are Failed")
else:
    print("Invalid marks")