#This project is about to create a to-do list in python

# print("Enter
# user_text=input()
# print(user_text)



todos = []

while True :
    user_action = input("Type add,show or exit: ")
    user_action = user_action.strip()  #strip() function is used for stripping trailing spaces

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)

        case 'show':
            for item in todos:
                print(item)

        case 'exit':
            break

        case x:
            print("Hey, you have entered a wrong command")


print("Bye!")
