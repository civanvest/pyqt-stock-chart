import streamlit as st
from pyrich.connect import Database


CONFIG = st.secrets['postgres']
st.title('Portfolio')

db = Database(CONFIG)

st.header('Summary')
st.write('show summary here')
# result = db.run('SELECT * FROM orders')
# st.dataframe(result)

st.header('Details')
st.write('show details here')

st.header('Visualization')
st.write('show visualization here')