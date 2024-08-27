import streamlit as st
import requests
from helpers.global_variables import MARKET_URL
from helpers.help_request import custom_post
from helpers import create_sidebar

def is_valid(name, city):
    if name and city:
        return False
    else:
        return True
    
st.set_page_config(
        page_title="CADASTRO de supermercado",
        layout="wide"
)

logged = create_sidebar()
    
if logged:
    st.title("Cadastrar um supermercado")
    st.header(":blue[]", divider="violet")

    name = st.text_input(label="Nome do supermercado: ")
    city = st.text_input(label="Cidade do supermercado: ")

    button_disabled = is_valid(name, city)
    if st.button(label="Cadastrar supermercado", disabled=button_disabled):
        custom_post(MARKET_URL, data={"name":name, "city": city})
