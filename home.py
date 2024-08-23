import streamlit as st
import requests
import json
import pandas as pd
import plotly.express as px

st.write("Hello")

response = requests.get("http://127.0.0.1:8000/market/supermarketController/")
response_dict = json.loads(response.text)

df = pd.DataFrame(response_dict["results"])[["name", "city"]]
p = df.value_counts("city").reset_index()
p

fig = px.pie(df.value_counts("city").reset_index(), values='count', names='city', title='Distribuition of supermarkets registered in the system')
st.plotly_chart(fig, use_container_width=True)

# for k, v in .items():
#     st.write(k, v)
