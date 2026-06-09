#This project is about to create a to-do list in python

todos = []

while True :
    user_action = input("Type add,show,edit or exit: ")
    user_action = user_action.strip()  #strip() function is used for stripping trailing spaces

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)

        case 'show':
            for item in todos:
                print(item)

        case 'edit':
            number = int(input("Number of todo to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo

        case 'exit':
            break

        case x:
            print("Hey, you have entered a wrong command")


print("Bye!")
