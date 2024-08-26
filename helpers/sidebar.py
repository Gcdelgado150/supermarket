import streamlit as st
from datetime import datetime
import pickle
import os
    
def create_sidebar():
    st.sidebar.image("data/images/logo.png", width=100)
    st.sidebar.title("Supermarket Controller")

    st.sidebar.page_link("home.py", 
                         label=":house: Inicio")
    
    # st.sidebar.page_link("pages/login.py", 
    #                      label=":house: Login")
    
    st.sidebar.page_link("pages/analysis.py", 
                         label=":chart: Análises") 
    
    st.sidebar.page_link("pages/stock.py", 
                         label=":chart: Checar estoques") 
    st.sidebar.divider()

    with st.sidebar.expander("Cadastros:", expanded=True):
        st.page_link("pages/add_customer.py", 
                             label=":adult: Cadastrar Cliente")
        
        st.page_link("pages/add_market.py", 
                             label=":shopping_trolley: Cadastrar Supermercado")
        
        st.page_link("pages/add_categories.py", 
                             label=":shopping_bags: Cadastrar Categoria de Produto")
        
        st.page_link("pages/products.py", 
                             label=":handbag: Cadastrar Produto")
        
        st.page_link("pages/stock_controller.py", 
                             label=":money_with_wings: Cadastrar um estoque")
        
    st.sidebar.page_link("pages/add_shopping.py",
                            label=":moneybag: Vender")

    st.sidebar.divider()