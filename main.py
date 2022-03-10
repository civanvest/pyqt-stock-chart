import pandas as pd
import streamlit as st
from pyrich.connect import Database


CONFIG = st.secrets['postgres']
st.title('Streamlit Application')

db = Database(CONFIG)

st.sidebar.title('Sidebar Title')
form = st.sidebar.form(key='my-form')
symbol = form.text_input('Symbol')
symbol = symbol.upper()
search = form.form_submit_button('Search')
if search:
    result = db.run('SELECT * FROM orders')
    st.dataframe(result)