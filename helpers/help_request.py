from .global_variables import *
import requests
import json
import streamlit as st

def custom_get(url):
    """
    
    """
    try:
        res = requests.get(BASE_URL + url)
    except:
        st.error("Backend fora do ar!")
    else:
        res = json.loads(res.text)
        return res

    return None

def custom_post(url, data):
    """
    
    """
    try:
        response = requests.post(BASE_URL + url, json=data)
    except:
        st.error("Backend não responde!")
    else:
        if response.status_code == 201:
            st.success('Registered!', icon="✅")
        if response.status_code == 400:
            st.error(response.text)

