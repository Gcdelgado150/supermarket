from http.cookies import SimpleCookie
import streamlit as st
import requests
from .global_variables import BASE_URL, USER_INFO_URL

class CookieManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(CookieManager, cls).__new__(cls, *args, **kwargs)
            cls._instance.cookies = {}
        return cls._instance

    def _parse_cookies(self, set_cookie_header):
        cookies = {}
        # Split the header by commas (handle multiple cookies in one header)
        cookie_parts = set_cookie_header.split(', ')
        
        for part in cookie_parts:
            # Split each part by ';' and take the first segment
            name_value = part.split(';')[0]
            
            # Split by '=' to get name and value
            if '=' in name_value:
                name, value = name_value.split('=', 1)
                cookies[name.strip()] = value.strip()
        
        return cookies
    
    def update_from_response(self, response):
        cookies = self._parse_cookies(response.headers.get('Set-Cookie', ''))
        self.cookies.update({key: morsel for key, morsel in cookies.items()})

    def get_cookie(self, name):
        print("Getting cookie: ", name)
        return self.cookies.get(name, None)
    
    def get_cookies(self):
        print("Getting cookies..")
        print(self.cookies)
        return self.cookies

    def clear_cookies(self):
        print("Clearing cookies..")
        self.cookies = {}

cookie_manager = CookieManager()

def get_user_info_from_session():
    global cookie_manager

    # Retrieve session ID from cookies
    session_id = cookie_manager.get_cookie('sessionid')
    if not session_id:
        # st.sidebar.write("No session ID found.")
        return False

    # Request to the Django API to get user info
    try:
        response = requests.get(f'{BASE_URL}/{USER_INFO_URL}', cookies={'sessionid': session_id})
        if response.status_code == 200:
            user_info = response.json()
            st.session_state['username'] = user_info.get('username')
            st.session_state['authenticated'] = True
            return True
        else:
            st.sidebar.write("Unable to retrieve user information.")
            return False
    except requests.RequestException as e:
        st.sidebar.write(f"Error: {e}")
        # main_login()
        return False