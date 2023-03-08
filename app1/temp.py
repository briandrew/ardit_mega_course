import PySimpleGUI as sg

button_labels = ("add", "edit", "apply", "end", "cancel", "undo", "redo")

layout = []

for label in button_labels:
    layout.append([sg.Button(label)])

window = sg.Window("My To=Do App", layout=layout)
window.read()
window.close()

