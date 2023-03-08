
# from functions import get_todos, write_todos  # I put functions in functions.py
import functions  # can use to explicitly call ie functions.get_todos
import time
print(f"It is {time.strftime('%b %d, %Y %H:%M:%S')}")

while True:
    user_action = input("Type add, show, edit, complete, or exit:  ").lower()
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')  # add break line to ToDos are on different lines in the txt file

        functions.write_todos(todos)  # no need to put in 2nd argument if the default works

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')  # remove break line
            row = f'{index + 1} - {item}'
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"ToDo '{todo_to_remove}' was removed from list"
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
    
    elif user_action.startswith('exit'):
        break
    else:
        print("command is not valid")
