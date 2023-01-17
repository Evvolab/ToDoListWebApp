# Imports
import streamlit as st
import functions

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

st.text_input(label = '', placeholder='Add new to-do')


