import streamlit as st
import requests
import json
import pandas as pd
import plotly.express as px
from helpers import create_sidebar
from helpers.global_variables import BASE_URL, PRODUCTS_URL, CATEGORIES_URL, MARKET_URL, STOCK_URL

st.set_page_config(
        page_title="Analysis",
)

create_sidebar()

response = requests.get(BASE_URL + MARKET_URL)
response_dict = json.loads(response.text)

df = pd.DataFrame(response_dict["results"])[["name", "city"]]
p = df.value_counts("city").reset_index()
p

fig = px.pie(df.value_counts("city").reset_index(), 
             values='count', 
             names='city', 
             title='Distribuition of supermarkets registered in the system')
st.plotly_chart(fig, use_container_width=True)

response = requests.get(BASE_URL + PRODUCTS_URL)
response_dict = json.loads(response.text)

df = pd.DataFrame(response_dict["results"])[["name", "value", "category"]]
p = df.value_counts("category").reset_index()
p

fig = px.pie(df.value_counts("category").reset_index(), 
             values='count', 
             names='category', 
             title='Distribuition the categories of the products registered')
st.plotly_chart(fig, use_container_width=True)