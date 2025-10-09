# This program is about a piggy bank

piggy_bank_balance = 100
cost_per_item = 10

while piggy_bank_balance > 0:
    print(f"Remining Balance: ${piggy_bank_balance}")
    piggy_bank_balance -=cost_per_item
print("You have spent all your saved money. ")