from playground import generate_response
import playground as pg
import streamlit as st

st.title('🦜🔗 Resumidor de textos:')

pg.openai_api_key = st.sidebar.text_input('OpenAI API Key')

with st.form('my_form'):
  text = st.text_area('Introduce el texto a resumir:', height=200)
  submitted = st.form_submit_button('Enviar')
  if not pg.openai_api_key.startswith('sk-'):
    st.warning('Introduce un key valido de OpenAI', icon='⚠')
  if submitted and pg.openai_api_key.startswith('sk-'):
    response = generate_response(text)
    st.info(response)