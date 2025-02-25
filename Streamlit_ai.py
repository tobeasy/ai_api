import streamlit as st
import Request_distributor
import database

# Initialize Request_distributor and Database instances in session state if not already done
if 'request_distributor' not in st.session_state:
    st.session_state.request_distributor = Request_distributor.Request_distributor()

if 'database' not in st.session_state:
    st.session_state.database = database.Database()

request_distributor = st.session_state.request_distributor
database = st.session_state.database

st.title('Universal AI Client')

options = ['Gemini 2.0 Flash', 'Gemini-2.0-flash-lite Preview', 'Gemini 1.5 Flash', 'Deepseek']
selected_option = st.selectbox('Select an AI model:', options)

api_key = st.text_input("Api_key:")
if st.button('Save api-key'):
    database.add_entry(selected_option, api_key)

if st.button('Delete api-key'):
    database.remove_entry(selected_option)

user_input = st.text_input("Gib etwas ein:")

if st.button('Senden'):
    api_key = database.get_api_key(selected_option)
    response = request_distributor.send_request(selected_option, user_input, api_key)
    st.write(response)

if st.button('Show all api-keys'):
    st.write(database.get_all_entries())