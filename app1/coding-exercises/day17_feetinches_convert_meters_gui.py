import PySimpleGUI as sg
from convertersd14 import convert


label1 = sg.Text("Enter feet:"),
input1 = sg.InputText(key="feet")

label2 = sg.Text("Enter inches:")
input2 = sg.InputText(key="inches")

convert_button = sg.Button("Convert")
output_label= sg.Text("", key="output", text_color="black")

exit_button = sg.Button("Exit")

window = sg.Window("Converter", layout=[[label1, input1], [label2, input2],[convert_button, exit_button, output_label]])


while True:
    event, values = window.read()

    match event:
        case "Exit":
            break

    print(event, values)
    try:
        feet = float(values["feet"])
        inches = float(values["inches"])
        result = convert(feet, inches)
        window["output"].update(value=f"{result} m", text_color="white")
    except ValueError:
        sg.Popup("Please enter feet and inches")
        continue


# window.read()


# window.close()
