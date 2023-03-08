import PySimpleGUI as sg
from extractor import extract_archive


# first row
label_select_archive = sg.Text("Select archive:")
input_archive_path = sg.Input()
choose_archive_path = sg.FileBrowse("Choose", key="archive")  # notice it is singular - sg.FileBrowse


# second row
label_select_destination = sg.Text("Select destination:")
input_destination_path = sg.Input()
choose_destination_path = sg.FolderBrowse("Choose", key="folder")

# third row
extract_button = sg.Button("Unzip")
label_success_fail = sg.Text("", key="output", text_color="black")  # place to present success/fail message
exit_button = sg.Button("Exit")

# add columns to align field in UI
col1 = sg.Column([[label_select_archive], [label_select_destination]])
col2 = sg.Column([[input_archive_path], [input_destination_path]])
col3 = sg.Column([[choose_archive_path], [choose_destination_path]])

# window = sg.Window("File Compressor",
#                    layout=[[label_select_archive, input_archive_path, choose_archive_path],
#                            [label_select_destination, input_destination_path, choose_destination_path],
#                            [extract_button, label_success_fail],
#                            [exit_button]])

window = sg.Window("Unzipper", layout=[[col1, col2, col3], [extract_button, exit_button]])

while True:
    event, values = window.read()
    print(event, values)
    archive_path = values["archive"]
    destination_folder = values["folder"]
    match event:
        case "Exit":
            break
    try:
        extract_archive(archive_path, destination_folder)
        window["output"].update(value="Unzip complete.")
    except FileNotFoundError:
        sg.popup("You did not enter a valid archive or folder")
        continue


# window.read()
# window.close()
