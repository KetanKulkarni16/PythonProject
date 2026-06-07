#This project is about to create a to-do list in python

# print("Enter
# user_text=input()
# print(user_text)

user_prompt = 'Enter todo:'

todos = []

while True :
    todo = input(user_prompt)
    print(todo.capitalize())
    todos.append(todo)