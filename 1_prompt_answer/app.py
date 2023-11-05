import playground
import streamlit as st

st.title('🦜🔗 Tu primera aplicación')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

with st.form('my_form'):
  prompt = st.text_area('Introduce texto:', 'Cuales son las bases para aprender Inteligencia Artificial?')
  submitted = st.form_submit_button('Enviar')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    response = generate_response(prompt)
    st.info(response)