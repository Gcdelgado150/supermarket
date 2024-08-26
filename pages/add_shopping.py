import streamlit as st
from helpers import PRODUCTS_URL, CUSTOMER_URL, MARKET_URL, PURCHASES_URL
from helpers.help_request import custom_get, custom_post
import pandas as pd
from helpers import create_sidebar
from datetime import datetime

def create_new_product(i):
    cols = st.columns(2)
    with cols[0]:
        product =  st.selectbox(label="Produto:", 
                                options=df_products.name.unique(), 
                                index=None,
                                placeholder="Escolha um Produto...",
                                key=f"product {i}")
    with cols[1]:
        amount = st.number_input(
            label="Quantidade:",
            value=0,  # Default value
            format=f"%d",  # Format to display the number
            step=1,
            key=f"amount {i}"
        )

    return product, amount

st.set_page_config(
        page_title="Shopping",
        layout="wide"
)

create_sidebar()
st.title("Fazer compras")
st.header(":blue[]", divider="violet")

res_customer = custom_get(CUSTOMER_URL)
res_market = custom_get(MARKET_URL)
res_products = custom_get(PRODUCTS_URL)

if res_market and res_customer and res_products:
    df_markets = pd.DataFrame(res_market["results"])
    df_customers = pd.DataFrame(res_customer["results"])
    df_products = pd.DataFrame(res_products["results"])

    cols = st.columns(2)
    with cols[0]:
        customer = st.selectbox(label="Cliente:",   
                                options=df_customers.name.unique(), 
                                index=0,
                                placeholder="Escolha um Cliente...")
    with cols[1]:
        supermarket = st.selectbox(label="Supermercado:",  
                                options=df_markets.name.unique(), 
                                index=None,
                                placeholder="Escolha um Supermercado...")
    
    all_products = []
    all_amounts = []

    st.header("Lista de compras")
    with st.container(border=True):
        while 1:
            product, amount = create_new_product(i=len(all_products))

            if amount:
                all_products.append(product)
                all_amounts.append(amount)
            else:
                break
    
    payment_options = ['C', 'D', 'P']
    payment_choices = ['Crédito', 'Débito', 'Pix']
    
    payment_method = st.radio("Método de pagamento:", options=payment_choices)
    payment_method = payment_options[payment_choices.index(payment_method)]
    
    if st.button(label="Fazer compras"):
        for product, amount in zip(all_products, all_amounts):
            custom_post(PURCHASES_URL, data={"customer":customer, 
                                        "supermarket": supermarket,
                                        "product": product,
                                        "amount": amount,
                                        "date": datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                                        "payment_method" :payment_method})


