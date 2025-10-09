#This program is about to print the consonants on string

word = input("Enter a word to check = ")
count = 0
vowels = "aeiou"
index = 0

while index < len(word):
    if word[index].lower() not in vowels and word[index].isalpha():
        count+=1
    index += 1
print("Number of consonants: ", count)