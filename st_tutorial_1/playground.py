# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: tags,-all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# (Inspirado en [LangChain tutorial #1: Build an LLM-powered app in 18 lines of code](https://blog.streamlit.io/langchain-tutorial-1-build-an-llm-powered-app-in-18-lines-of-code/))

# %% [markdown]
# # Tu primera App Con Langchain. 
# ### Prompt-Answer

# %% [markdown]
# ## Paso 1. Obteniendo una llave de OpenAI
#
# - Navega a [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
# - Haz click en "Create new secret key"
# - Dale un nombre e insertalo en la celda de abajo
#
# !["OpenAI key"](assets/openai_key.png)

# %% [markdown]
# <span style="color:red;">IMPORTANTE: Nunca subas código a github con llaves privadas!</span>

# %%
global openai_api_key
openai_api_key="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"

# %% [markdown]
# ## Paso 2. Instala las librerías necesarias
# - streamlit: permite crear aplicaciones web interactivas de manera sencilla
# - langchain: permite integrar los modelos de lenguaje de OpenAI en aplicaciones de forma simple
# - openai: permite comunicarse con el api de openai

# %%
# %pip install streamlit openai langchain 

# %% [markdown]
# ## Paso 3. Creamos una función para llamar a la API de OpenAI mediante LangChain
# (OpenAI no es el único modelo que podemos usar)

# %%
from langchain.llms import OpenAI
# from langchain.llms import Anthropic

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  # llm = Anthropic(anthropic_api_key=anthropic_api_key)
  return llm(input_text)

# %% tags=["active-ipynb"]
# prompt = """
#     Dime de forma breve lo que puede hacer el api de openai
# """

# %% tags=["active-ipynb"]
# response = generate_response(prompt)
# print(response)

# %% [markdown]
# ## Paso 4. Creamos nuestra app en Streamlit usando la funcion generate_response
#
# - crea un nuevo archivo app.py
# - nuestra app hará uso de las funciones de streamlit:
#   - [st.title](https://docs.streamlit.io/library/api-reference/text/st.title)
#   - [st.form](https://docs.streamlit.io/library/api-reference/control-flow/st.form)
#   - [st.text_area](https://docs.streamlit.io/library/api-reference/widgets/st.text_area)
#   - [st.form_submit_button](https://docs.streamlit.io/library/api-reference/control-flow/st.form_submit_button)
#   - [st.info](https://docs.streamlit.io/library/api-reference/status/st.info)
#   - [st.warning](https://docs.streamlit.io/library/api-reference/status/st.warning)

# %% [markdown]
# ## Paso 5. Ejecuta la aplicación
# (También puedes ejecutarla ene una terminal aparte si así lo prefieres)

# %% language="bash"
# streamlit run app.py

# %% [markdown]
# ![Explanation](assets/explanation.png)

# %% [markdown]
#
