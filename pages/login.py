import streamlit as st
import requests

# Django API base URL
API_URL = 'http://localhost:8000/api/accounts/'

# Streamlit UI
st.title('Login Page')

def register():
    username = st.text_input('Username')
    email = st.text_input('Email')
    password = st.text_input('Password', type='password')
    
    if st.button('Register'):
        response = requests.post(f'{API_URL}register/', data={'username': username, 'email': email, 'password': password})
        if response.status_code == 201:
            st.success('User created successfully')
        else:
            st.error('Error creating user')
            st.error(response.text)

def login():
    username = st.text_input('Username', key='login')
    password = st.text_input('Password', type='password', key='login_password')
    
    if st.button('Login'):
        response = requests.post(f'{API_URL}login/', data={'username': username, 'password': password})
        if response.status_code == 200:
            st.success('Login successful')
        else:
            st.error('Invalid credentials')
            st.error(response)

option = st.selectbox('Select action', ['Login', 'Register'])

if option == 'Register':
    register()
else:
    login()