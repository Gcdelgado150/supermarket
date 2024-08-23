import streamlit as st
import requests
from helpers import BASE_URL, CATEGORIES_URL
import pandas as pd
import json
from helpers import create_sidebar

st.set_page_config(
        page_title="Shopping",
)

create_sidebar()