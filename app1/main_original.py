

# todos = [] - don't need list anymore, saving todos to txt file
# user_action = ''

while True:
    user_action = input("Type add, show, edit, complete, or exit:  ").lower()
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + '\n'  # the \n adds a break line to send to txt file one on each line

            with open('todos.txt', 'r') as file:
                todos = file.readlines()  # creates list of items in the file
            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            if not todos:
                print("You don't have any todos yet.")
            else:
                print()
                print("Your ToDos are: ")
                print('-' * 20)
            for index, item in enumerate(todos):
                item = item.strip('\n')  # remove break line
                print(f'ToDo {index+1}: {item.capitalize()}')

        case 'edit':
            number = int(input("Which number task to you want to edit: "))
            number = number - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Which number task to you want to complete: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"ToDo '{todo_to_remove}' was removed from list"
            print(message)

        case 'exit':
            break
        case input_error:
            print("That was not add, show, edit, or exit")

