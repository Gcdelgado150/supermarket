import streamlit as st
import pandas as pd
import plotly.express as px
from helpers import create_sidebar
from helpers.global_variables import STOCK_URL, MARKET_URL
from helpers.help_request import custom_get

st.set_page_config(
        page_title="Stock",
)

create_sidebar()

res_stock = custom_get(STOCK_URL)
res_supermarket = custom_get(MARKET_URL)

if res_stock and res_supermarket:
    df = pd.DataFrame(res_stock["results"])[["supermarket", "product", "amount"]]
    df_markets = pd.DataFrame(res_supermarket["results"])[["name"]]
    
    supermarket = st.radio("Selecione um supermercado", options=df_markets.name.unique())

    # analise do estoque desse supermercado

    fig1 = px.bar(df[df["supermarket"] == supermarket], x='product', y='amount')
    st.plotly_chart(fig1, use_container_width=True)
    