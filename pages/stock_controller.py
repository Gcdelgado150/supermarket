import streamlit as st
import pandas as pd
from helpers.global_variables import PRODUCTS_URL, MARKET_URL, STOCK_URL
from helpers.help_request import custom_get, custom_post
from helpers import create_sidebar

st.set_page_config(
        page_title="Stocks",
        layout="wide"
)

create_sidebar()
st.title("Adicionar um estoque")
st.write("Compramos um item do revendedor e queremos adicionar o produto no estoque")
st.header(":blue[]", divider="violet")

response_supermarket = custom_get(MARKET_URL)
response_products = custom_get(PRODUCTS_URL)

if response_supermarket and response_products: 
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
        custom_post(STOCK_URL, data={"supermarket":supermarket, 
                                     "product": product, 
                                     "amount": amount})


