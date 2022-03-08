import streamlit as st

st.title('Streamlit Application')

st.sidebar.title('Sidebar Title')
form = st.sidebar.form(key='my-form')
symbol = form.text_input('Symbol')
symbol = symbol.upper()
search = form.form_submit_button('Search')
if search:
    st.write(symbol)