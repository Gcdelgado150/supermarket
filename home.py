import streamlit as st
import requests
import json
import pandas as pd
import plotly.express as px
from helpers import create_sidebar
from helpers.global_variables import BASE_URL, PRODUCTS_URL, CATEGORIES_URL, MARKET_URL, STOCK_URL

create_sidebar()

st.write("This is the home page.")