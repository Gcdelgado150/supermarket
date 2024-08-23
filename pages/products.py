import streamlit as st
from helpers.global_variables import BASE_URL, PRODUCTS_URL, CATEGORIES_URL
import requests
import json
import pandas as pd

def verify_conditions():
    return False

response_categories = requests.get(BASE_URL + CATEGORIES_URL)
response_categories = json.loads(response_categories.text)
df = pd.DataFrame(response_categories["results"])[["name"]]

name = st.text_input(label="Name of the product: ")
value = st.number_input(
    label="Enter a value:",
    value=0.0,  # Default value
    format=f"%.2f",  # Format to display the number
    step=0.01  # Increment step, to match decimal places
)
category = st.selectbox("Category:", df.name.unique())
st.write(str(category))
# st.write()

button_disabled = verify_conditions()
if button_disabled:
    st.info(f"The product {name} with value {value} is invalid.")

if st.button(label="Add a product", disabled=button_disabled):
    requests.post(BASE_URL + PRODUCTS_URL, json={"name":name, 
                                                 "value": value, 
                                                 "category": str(category)})


