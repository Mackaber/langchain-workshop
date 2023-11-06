from playground import generate_response
import playground as pg
import streamlit as st

st.title('🦜🔗 lalala')

pg.openai_api_key = st.sidebar.text_input('OpenAI API Key')

with st.form('my_form'):
  # File upload
  uploaded_file = st.file_uploader('Carga un documento en PDF', type='pdf')  
  # Query text
  query_text = st.text_input('Enter your question:', placeholder = 'Please provide a short summary.')
  submitted = st.form_submit_button('Enviar')
  if not pg.openai_api_key.startswith('sk-'):
    st.warning('Introduce un key valido de OpenAI', icon='⚠')
  if submitted and pg.openai_api_key.startswith('sk-'):
    response = generate_response(uploaded_file.read(), query_text)
    st.info(response)