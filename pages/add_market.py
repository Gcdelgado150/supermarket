import streamlit as st
import requests
from helpers.global_variables import BASE_URL, MARKET_URL
from helpers import create_sidebar

st.set_page_config(
        page_title="Supermarkets",
)

create_sidebar()

name = st.text_input(label="Name of the market: ")
city = st.text_input(label="City of the market: ")

if st.button(label="Add market"):
    requests.post(BASE_URL + MARKET_URL, json={"name":name, "city": city})
