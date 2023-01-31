# Imports
import streamlit as st
import base64
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



# Background

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

    
add_bg_from_local('files/background.jpg') 


