import requests
from .global_variables import BASE_URL, LOGOUT_URL, LOGIN_URL, USER_INFO_URL
from .cookie_handler import cookie_manager
import streamlit as st

# Streamlit app UI
def main_login():
    # Define custom CSS for styling the login container
    st.markdown("""
        <style>
        .login-input {
            margin-bottom: 15px;
        }
        .login-button {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
        }
        .login-button:hover {
            background-color: #0056b3;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title('Login to Supermarket')

    with st.container(border=True):
        # Check authentication status
        if ('authenticated' not in st.session_state or 
            not st.session_state['authenticated']):
            
            username = st.text_input('Username', 
                                     key='username_input', 
                                     placeholder='Enter your username', 
                                     label_visibility='collapsed', 
                                     help='Your username')
            
            password = st.text_input('Password', 
                                     type='password', 
                                     key='password_input', 
                                     placeholder='Enter your password', 
                                     label_visibility='collapsed', 
                                     help='Your password')
            
            if st.button('Login', key='login', help='Click to log in', use_container_width=True):
                login(username, password)
        
def login(username, password):
    response = requests.post(f'{BASE_URL}/{LOGIN_URL}', data={'username': username, 'password': password})
    if response.status_code == 200:
        cookie_manager.update_from_response(response)
        st.session_state['authenticated'] = True
        st.session_state['username'] = username
        st.success('Login successful!')
        st.rerun()
    else:
        st.error('Login failed. Please check your credentials.')

def logout():
    cookies = cookie_manager.get_cookies()
    csrf_token = cookies.get("csrftoken")
    response = requests.post(f'{BASE_URL}/{LOGOUT_URL}', 
                             cookies=cookies,
                             headers = {'X-CSRFToken': csrf_token})
    if response.status_code == 200:
        cookie_manager.clear_cookies()
        st.session_state['authenticated'] = False
        st.session_state['username'] = None
        st.success('Logout successful!')
        main_login()
        st.rerun()
    else:
        st.error('Logout failed.')
        