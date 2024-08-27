import streamlit as st
import pandas as pd
from helpers.global_variables import CUSTOMER_URL, CATEGORIES_URL
from helpers.help_request import custom_get, custom_post
from helpers import create_sidebar
import re

def is_valid_cpf(cpf):
    """Validate CPF number using a simple check (not fully accurate, but a basic example)."""
    cpf = re.sub(r'\D', '', cpf)  # Remove non-digit characters
    if len(cpf) != 11 or cpf.isdigit() == False:
        return False
    return True

st.set_page_config(
        page_title="Cliente",
        layout="wide"
)

logged = create_sidebar()

if logged:
    st.title("Cadastrar um cliente à rede")
    st.header(":blue[]", divider="violet")

    name = st.text_input(label="Nome do cliente: ")
    cpf_input = st.text_input("CPF (somente números)", max_chars=11)

    gender_options = ['M', 'F']
    gender_choices = ['Male', 'Female']

    gender = st.radio("Gender:", options=gender_choices, horizontal=True)
    gender = gender_options[gender_choices.index(gender)]

    subs_options = ['R', 'P', 'S']
    subs_choices = ['Registered', 'Pay', 'Special']

    subscription_type = st.radio("Subscription:", options=subs_choices)
    subscription_type = subs_options[subs_choices.index(subscription_type)]


    button_disabled = is_valid_cpf(cpf_input)
    if cpf_input and not button_disabled:
        st.info(f"CPF: {cpf_input} is invalid.")

    if st.button(label="Add a customer", disabled=not button_disabled):
        custom_post(CUSTOMER_URL, data={"name":name, 
                                        "cpf": cpf_input,
                                        "gender": gender,
                                        "subscription_type": subscription_type})


