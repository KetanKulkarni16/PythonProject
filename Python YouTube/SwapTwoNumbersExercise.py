#This program is about to swap two numbers

a = input("Enter the Value of a: ")
b = input("Enter the value of b: ")

temp = a  #Taking a third variable/container TEMP and assigning the first value to it.
a= b
b = temp

print("After Swapping the two numbers: ")
print("a= " + a)
print("b= " + b)


#Rules for naming variables

#The variable name must be meaningful
#The name can be only start from A-Z, a-z, 0-9 and '_' underscore.
# NO other special symbols and whitespace are not allowed.
#Variable name can not start with digit.
#CAMEL CASE: myName,myVariableName
#SNAKE CASE: my_variable_name