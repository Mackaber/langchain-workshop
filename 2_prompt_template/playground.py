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
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# (Inspirado en [LangChain tutorial #2: Build a blog outline generator app in 25 lines of code](https://blog.streamlit.io/langchain-tutorial-2-build-a-blog-outline-generator-app-in-25-lines-of-code/))

# %% [markdown]
# # Una aplicación para "aprender cualquier cosa"
# ### PromptTemplate-Prompt-Answer

# %% [markdown]
# <span style="color:red;">IMPORTANTE: Nunca subas código a github con llaves privadas!</span>

# %%
openai_api_key = ""

# %% [markdown]
# ## Prompt templates:
#
# Un prompt template es una plantilla de texto que se utiliza para definir y componer funciones de inteligencia artificial (IA) en lenguaje natural. Estas plantillas se utilizan para crear prompts de lenguaje natural, generar respuestas, extraer información, invocar otros prompts o realizar cualquier otra tarea que pueda expresarse con texto
#
# Algunas características de los prompt templates son:
#
# - **Variables**: Se pueden incluir variables en las plantillas para que se inserten valores, funciones o variables en los prompts
# - **Llamadas a funciones externas**: Se pueden llamar a funciones externas desde las plantillas
# - **Pasaje de parámetros a funciones**: Se pueden pasar parámetros a las funciones desde las plantillas
#
# ![Template](assets/template.png)
#
# Algunos recursos:
#
# - [https://www.pinecone.io/learn/series/langchain/langchain-prompt-templates/](https://www.pinecone.io/learn/series/langchain/langchain-prompt-templates/)
# - [https://github.com/forReason/GPT-Prompt-Templates](https://github.com/forReason/GPT-Prompt-Templates)
# - [https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/](https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/)

# %% [markdown]
# ## Paso 1. Definamos un Template

# %%
template = """
  Como un profesor experto quiero que me propongas 
  una ruta de aprendizaje para aprender {topic}
"""

# %%
from langchain.llms import OpenAI
from langchain import PromptTemplate

def generate_response(topic):
  llm = OpenAI(temperature=0.7, model_name="gpt-3.5-turbo-instruct", openai_api_key=openai_api_key)
  prompt = PromptTemplate(input_variables=['topic'], template=template)
  prompt_query = prompt.format(topic=topic)
  return llm(prompt_query)

# %% tags=["active-ipynb"]
# topic = """
#     Computación Cuántica
# """

# %% tags=["active-ipynb"]
# response = generate_response(topic)
# print(response)

# %% [markdown]
# ## Paso 4. Creamos nuestra app en Streamlit usando la funcion generate_response (Es casi idéntica a la de st_tutorial_1)
#
# - crea un nuevo archivo app.py
# - nuestra app hará uso de las funciones de streamlit:
#   - [st.title](https://docs.streamlit.io/library/api-reference/text/st.title)
#   - [st.form](https://docs.streamlit.io/library/api-reference/control-flow/st.form)
#   - [st.text_input](https://docs.streamlit.io/library/api-reference/widgets/st.text_input)
#   - [st.form_submit_button](https://docs.streamlit.io/library/api-reference/control-flow/st.form_submit_button)
#   - [st.info](https://docs.streamlit.io/library/api-reference/status/st.info)
#   - [st.warning](https://docs.streamlit.io/library/api-reference/status/st.warning)

# %% [markdown]
# ## Paso 5. Ejecuta la aplicación
# (También puedes ejecutarla ene una terminal aparte si así lo prefieres)

# %%
# !streamlit run app.py

# %% [markdown]
# ![Explanation](assets/explanation.png)

# %% [markdown]
# ### Ideas adicionales
#
# - Distintos templates: 
#   - ¿Como contestarian distintas personas/agentes? (eg. filosofos)
# - Uso de dropdown en streamlit
# - Distintas variables dentro del template (eg. Recetas de cocina: tiempo e ingredientes)
