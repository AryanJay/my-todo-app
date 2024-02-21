import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n" # call the key of the pair to obtain the value
    todos.append(todo)
    functions.write_todos(todos) # write updated to-do in txt file

st.title("My Todo App")
st.subheader("This is my Todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index) # remove to-do for which the checkbox was chekced
        functions.write_todos(todos)
        del st.session_state[todo] # deletes selected pair
        st.rerun()

st.text_input(label="", placeholder="Add a todo...",
              on_change=add_todo, key="new_todo")