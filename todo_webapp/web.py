import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"  # to create break line, else added on same line
    todos.append(todo)
    functions.write_todos(todos)


# the order of these matters
st.title("My Todo App")
st.subheader("This is my Todo App")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)  # key is used by session state
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()  # required for check boxes

st.text_input(label="Enter ToDo: ", label_visibility="hidden", placeholder="Add a todo.....",
              on_change=add_todo, key="new_todo")

