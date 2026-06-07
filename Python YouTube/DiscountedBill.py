#This program is about Discount at Grocery shop


print("Grocery Store shopping counter")
amount = float(input("Enter the bill amount: "))

if amount <= 1000:
    amount = (amount - amount * 0.10)
    print('Discounted Bill: ', amount)
elif amount >= 1000 and amount <= 5000:
    amount = (amount - amount * 0.15)
    print("Discounted Bill", amount)
elif amount >= 5000 and amount <=10000:
     amount =  (amount - amount * 0.20)
     print("Discounted Bill", amount)
elif amount >=10000 and amount <=25000:
    amount = (amount - amount * 0.20)
    print("Discounted Bill", amount)
else:
    amount = (amount - amount * 0.25)
    print("Discounted Bill:", amount)