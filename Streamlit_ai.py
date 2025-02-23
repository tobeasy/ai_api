import os
import streamlit as st
import pandas as pd
import Request_distributor

request_distributor = Request_distributor.Request_distributor()

st.title('Universal AI Client')
st.write('This is a simple AI connector using Streamlit')

options = ['Gemini 2.0 Flash', 'Gemini-2.0-flash-lite Preview', 'Gemini 1.5 Flash', 'Deepseek']
selected_option = st.selectbox('Wähle eine KI:', options)

user_input = st.text_input("Gib etwas ein:")

if st.button('Senden'):
    response = request_distributor.send_request(selected_option, user_input)
    st.write(response)