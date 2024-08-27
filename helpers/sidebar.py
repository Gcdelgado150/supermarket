import streamlit as st
from .login_handler import logout, main_login
from .cookie_handler import get_user_info_from_session

def actual_sidebar():
    st.sidebar.image("data/images/logo.png", width=100)
    st.sidebar.title("Supermarket Controller")
    st.sidebar.write(f"Welcome back {st.session_state['username']}")

    st.sidebar.page_link("home.py", 
                        label=":house: Inicio")
    
    # st.sidebar.page_link("pages/login.py", 
    #                      label=":house: Login")
    
    # TODO: Adicionar if do grupo de usuario!
    st.sidebar.page_link("pages/analysis.py", 
                        label=":chart: Análises") 
    
    st.sidebar.page_link("pages/stock.py", 
                        label=":chart: Checar estoques") 
    st.sidebar.divider()
    
    # TODO: Adicionar if do grupo de usuario!
    with st.sidebar.expander("Cadastros:", expanded=True):
        st.page_link("pages/add_customer.py", 
                    label=":adult: Cadastrar Cliente")
        
        st.page_link("pages/add_market.py", 
                    label=":shopping_trolley: Cadastrar Supermercado")
        
        st.page_link("pages/add_categories.py", 
                    label=":shopping_bags: Cadastrar Categoria de Produto")
        
        st.page_link("pages/products.py", 
                    label=":handbag: Cadastrar Produto")
        
    # TODO: Adicionar if do grupo de usuario!
    with st.sidebar.expander("Compras:", expanded=True):
        st.page_link("pages/stock_controller.py", 
                    label=":money_with_wings: Cadastrar/Adicionar um estoque")
        
    # TODO: Adicionar if do grupo de usuario!
    with st.sidebar.expander("Vendas", expanded=False):
        st.page_link("pages/add_shopping.py",
                    label=":moneybag: Vender")

    st.sidebar.divider()

    if st.sidebar.button("Logout"):
        logout()

def create_sidebar():
    logged = get_user_info_from_session()

    if not logged:
        main_login()
        return False
    else:
        actual_sidebar()
        return True
    