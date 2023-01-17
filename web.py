# Imports
import streamlit as st
import functions

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

# Title
st.title('My Todo App')

# Subheader
st.subheader('This is the subheader')

# General Writeups
st.write('This app is to increase your productivity')

# Assign To-do Items to a list
todos = functions.get_todos()

# Iterate the todos list to add checkboxes 
for item in todos:
    st.checkbox(item)

st.text_input(label = 'input box', label_visibility='hidden', placeholder='Add new to-do',
        on_change= add_todo, key= 'new_todo')


