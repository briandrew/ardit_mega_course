"""build front-end gui for to-do list app """

import functions
import PySimpleGUI as sg
import time
import os  # in order to detect if todos.txt exist and if not create it

if not os.path.exists("todos.txt"):  # checks to see if todos.txt exists
    with open("todos.txt", "w") as file:  # creates todos.txt if not found
        pass

# sg.theme("green")

clock = sg.Text("", key="clock", font=("Helvetica", 8))

label = sg.Text("Type in a ToDo:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")

add_button = sg.Button("Add", mouseover_colors="red", tooltip="Add ToDo", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))  # 45 char wide by 10 char height(rows)

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete", mouseover_colors="red", tooltip="Complete ToDo",
                            key="Complete")
exit_button = sg.Button("Exit")


window = sg.Window('My ToDo App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 15), )  # each inside [] is a row

while True:
    event, values = window.read(timeout=500)  # method to display the window & millisecond refresh
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M"))  # don't need seconds displayed

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.Popup("Please select an item first.", font=("Helvetica", 15))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()  # 'todos' is a list so use the .remove method to 'complete'
                todos.remove(todo_to_complete)
                functions.write_todos(todos)  # send to write_todos function to write to the .txt
                window['todos'].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.Popup("Please select an item first.", font=("Helvetica", 15))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

# window.close()  # method to close the window when press close button
