#This program is about to count the occurances in string

string = input("Enter a string = ")
char_to_count = input("Enter a character to count =  ")
count = 0
index = 0

while index < len(string):
    if string[index] == char_to_count:
        count += 1
    index += 1
print(f"{char_to_count} = {count}")