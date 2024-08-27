from helpers import create_sidebar, main_login
from helpers.cookie_handler import get_user_info_from_session
import streamlit as st

def home():
    create_sidebar()
    st.write(f"You're welcome {st.session_state['username']}.")

if __name__ == "__main__":
    logged = get_user_info_from_session()

    if not logged:
        main_login()
    else:
        home()
