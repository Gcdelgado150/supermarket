import streamlit as st
import requests
from helpers import BASE_URL, CATEGORIES_URL
import pandas as pd
import json
from helpers import create_sidebar

st.set_page_config(
        page_title="Categories",
)

create_sidebar()

name = st.text_input(label="Name of the category: ")
description = st.text_area(
    label="Description of the category:",
    height=200,  # Adjust the height of the text area
    placeholder="Description of the category..."  # Placeholder text
)

response_categories = requests.get(BASE_URL + CATEGORIES_URL)
response_categories = json.loads(response_categories.text)
df = pd.DataFrame(response_categories["results"])
df["name"] = df["name"].str.lower()

button_disabled = name.lower() in df.name.unique()
if button_disabled:
    st.info(f"The category {name} trying to be add already exists")

if st.button(label="Add category", disabled=button_disabled):
    requests.post(BASE_URL + CATEGORIES_URL, json={"name":name, "description": description})
