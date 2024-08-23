import streamlit as st
import requests
import json

response_supermarket = requests.get("http://127.0.0.1:8000/market/supermarketController/")
response_stock = requests.get("http://127.0.0.1:8000/market/stockController/")

response_stock = json.loads(response_stock.text)
st.write(response_stock)