from playground import generate_response
import playground as pg
import streamlit as st

st.title('🦜🔗 Quiero aprender de:')

pg.openai_api_key = st.sidebar.text_input('OpenAI API Key')

with st.form('my_form'):
  topic = st.text_input('Introduce algun tema:')
  submitted = st.form_submit_button('Enviar')
  if not pg.openai_api_key.startswith('sk-'):
    st.warning('Introduce un key valido de OpenAI', icon='⚠')
  if submitted and pg.openai_api_key.startswith('sk-'):
    response = generate_response(topic)
    st.info(response)