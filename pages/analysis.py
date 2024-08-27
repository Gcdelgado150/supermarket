import streamlit as st
import pandas as pd
import plotly.express as px
from helpers import create_sidebar
from helpers.global_variables import PRODUCTS_URL, MARKET_URL, CUSTOMER_URL
from helpers.help_request import custom_get

st.set_page_config(
        page_title="Analysis",
)

logged = create_sidebar()

if logged:
        res_market = custom_get(MARKET_URL)

        if res_market:
                df = pd.DataFrame(res_market["results"])[["name", "city"]]
                p = df.value_counts("city").reset_index()

                fig = px.pie(df.value_counts("city").reset_index(), 
                        values='count', 
                        names='city', 
                        title='Distribuition of supermarkets registered in the system')
                st.plotly_chart(fig, use_container_width=True)

        res_products = custom_get(PRODUCTS_URL)

        if res_products:
                df = pd.DataFrame(res_products["results"])[["name", "value", "category"]]
                p = df.value_counts("category").reset_index()

                fig = px.pie(df.value_counts("category").reset_index(), 
                        values='count', 
                        names='category', 
                        title='Distribuition the categories of the products registered')
                st.plotly_chart(fig, use_container_width=True)

        res_customers = custom_get(CUSTOMER_URL)
        if res_customers:
                df = pd.DataFrame(res_customers["results"])
                p = df.value_counts("subscription_type").reset_index()

                fig = px.pie(df.value_counts("subscription_type").reset_index(), 
                        values='count', 
                        names='subscription_type', 
                        title='Distribuition the subscription_type of the products registered')
                st.plotly_chart(fig, use_container_width=True)