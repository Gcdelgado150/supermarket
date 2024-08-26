import streamlit as st
from helpers import CATEGORIES_URL
from helpers.help_request import custom_get, custom_post
import pandas as pd
from helpers import create_sidebar

def is_valid(name, df, description):
    if name and description:
        if name.lower() in df.name.unique():
            st.info(f"The category {name} trying to be add already exists")
            return True
        else:
            return False
    else:
        return True
    
st.set_page_config(
        page_title="Categories",
        layout="wide"
)

create_sidebar()

st.title("Adicionar uma categoria de produtos")
st.header(":blue[]", divider="violet")

response_categories = custom_get(CATEGORIES_URL)

if response_categories:
    name = st.text_input(label="Name of the category: ")
    description = st.text_area(
        label="Description of the category:",
        height=200,  # Adjust the height of the text area
        placeholder="Description of the category..."  # Placeholder text
    )

    df = pd.DataFrame(response_categories["results"])
    df["name"] = df["name"].str.lower()

    button_disabled = is_valid(name, df, description)

    if st.button(label="Add category", disabled=button_disabled):
        custom_post(CATEGORIES_URL, data={"name":name, "description": description})
