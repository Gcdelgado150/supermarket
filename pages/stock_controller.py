import streamlit as st
import requests
import json
import pandas as pd
from helpers.global_variables import BASE_URL, PRODUCTS_URL, MARKET_URL, STOCK_URL
from helpers import create_sidebar

st.set_page_config(
        page_title="Stocks",
)

create_sidebar()

response_supermarket = requests.get(BASE_URL + MARKET_URL)
response_products = requests.get(BASE_URL + PRODUCTS_URL)

response_supermarket = json.loads(response_supermarket.text)
response_products = json.loads(response_products.text)

df_markets = pd.DataFrame(response_supermarket["results"])
df_products = pd.DataFrame(response_products["results"])

supermarket = st.selectbox(label="Name:", 
                           options=df_markets.name.unique(), 
                           index=None,
                           placeholder="Escolha um Supermercado...")
product =  st.selectbox(label="Name:", 
                        options=df_products.name.unique(), 
                           index=None,
                        placeholder="Escolha um Produto...")

amount = st.number_input(
    label="Enter amount:",
    value=0,  # Default value
    format=f"%d",  # Format to display the number
    step=1  # Increment step, to match decimal places
)

if st.button(label="Add a stock"):
    response = requests.post(BASE_URL + STOCK_URL, json={"supermarket":supermarket, 
                                                 "product": product, 
                                                 "amount": amount})
    if response.status_code == 201:
        st.success('Stock product registered!', icon="✅")
    if response.status_code == 400:
        st.error(response.text)


