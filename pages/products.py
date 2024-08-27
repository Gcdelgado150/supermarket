import streamlit as st
import pandas as pd
from helpers.global_variables import PRODUCTS_URL, CATEGORIES_URL
from helpers.help_request import custom_get, custom_post
from helpers import create_sidebar

st.set_page_config(
        page_title="Products",
        layout="wide"
)

logged = create_sidebar()
    
if logged:
    st.title("Adicionar um produto à um supermercado existente")
    st.header(":blue[]", divider="violet")

    def verify_conditions():
        """False is to enable button (valid conditions)
        True is for disable button (invalid conditions)"""
        return False

    response_categories = custom_get(CATEGORIES_URL)

    if response_categories:
        df = pd.DataFrame(response_categories["results"])[["name"]]

        name = st.text_input(label="Name of the product: ")
        value = st.number_input(
            label="Enter a value:",
            value=0.0,  # Default value
            format=f"%.2f",  # Format to display the number
            step=0.01  # Increment step, to match decimal places
        )
        category = st.selectbox("Category:", df.name.unique())

        button_disabled = verify_conditions()
        if button_disabled:
            st.info(f"The product {name} with value {value} is invalid.")

        if st.button(label="Add a product", disabled=button_disabled):
            custom_post(PRODUCTS_URL, data={"name":name, 
                                            "value": value,
                                            "category": str(category)})


