import streamlit as st
from datetime import datetime
import pickle
import os
    
def create_sidebar():
    st.sidebar.image("data/images/logo.png", width=100)
    st.sidebar.title("Supermarket Controller")

    st.sidebar.page_link("home.py", 
                         label=":house: Inicio")
    
    st.sidebar.page_link("pages/analysis.py", 
                         label=":chart: Análises") 
    st.sidebar.divider()

    with st.sidebar.expander("Adicionar:", expanded=True):
        st.sidebar.page_link("pages/add_market.py", 
                             label=":shopping_trolley: Adicionar Supermercado")
        
        st.sidebar.page_link("pages/add_categories.py", 
                             label=":shopping_bags: Adicionar Categoria de Produto")
        
        st.sidebar.page_link("pages/products.py", 
                             label=":handbag: Adicionar Produto")
        
        st.sidebar.page_link("pages/stock_controller.py", 
                             label=":money_with_wings: Adicionar um produto à um estoque")
        
        st.sidebar.divider()

        st.sidebar.page_link("pages/add_shopping.py",
                             label=":moneybag: Vender")

    st.sidebar.divider()