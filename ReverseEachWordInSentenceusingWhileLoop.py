#This program is about to reverse a each word in a sentence

sen = input("Enter a sentence: ")
words = sen.split()

for word in words:
    i = len(word) - 1
    while i >=0:
        print(word[i], end=" ")
        i-=1
    print(end= " ")

