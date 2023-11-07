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
# (Esta parte es necesaria para evitar un bug que actualmente ocurre con la librería chromadb)

# %%
__import__('pysqlite3')
import os
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join('.', 'db.sqlite3'),
    }
}

# %% [markdown]
# (Inspirado en [LangChain tutorial #4: Build an Ask the Doc app](https://blog.streamlit.io/langchain-tutorial-4-build-an-ask-the-doc-app/))

# %% [markdown]
# # Platica con tus documentos
# ### Documents

# %% [markdown]
# <span style="color:red;">IMPORTANTE: Nunca subas código a github con llaves privadas!</span>

# %%
openai_api_key=""

# %% [markdown]
# ## Paso 1. Instalamos pypdf y chromadb
# - [ChromaDB](https://docs.trychroma.com): ChromaDB es una base de datos de vectores de código abierto que se utiliza para almacenar y recuperar incrustaciones de vectores
# - pypdf: es una biblioteca gratuita y de código abierto de Python que se utiliza para trabajar con archivos PDF.
#

# %%
# %pip install pypdf chromadb 

# %% [markdown]
# ## Paso 2. Generamos un campo para subir el archivo con ipywidgets
# (Éste sólo será necesario para el notebook, en streamlit se subirán de otra forma)

# %% tags=["active-ipynb"]
# from ipywidgets import FileUpload
# from IPython.display import display
#
# uploader = FileUpload()
# display(uploader)

# %% [markdown]
# ## Paso 3. Definimos una función para dividir el documento
# - `PyPDFLoader` es un loader de documentos de pdf dentro de LangChain que utiliza pypdf
# - Ya que `PyPDFLoader` requiere que le pasemos la ruta de un archivo, generamos éste en memoria con `tempfile` y `shutil`
# - Por úlitmo dividimos el archivo en `Document`s justo como lo hicimos en el tutorial previo

# %%
from langchain.document_loaders import PyPDFLoader
from io import BytesIO
import tempfile
import shutil

def split_document(uploaded_file):
  # Copy the file in memory to a temp location 
  file_bytes = BytesIO(uploaded_file)
  file = tempfile.NamedTemporaryFile(delete=False)
  shutil.copyfileobj(file_bytes, file)
  # Specify the loader and split the file into multiple documents
  loader = PyPDFLoader(file.name)
  documents = loader.load_and_split()
  return documents


# %% [markdown]
# ## Paso 4. Probamos nuestra función

# %% tags=["active-ipynb"]
# uploaded_file = uploader.value[0].content.tobytes()
# split_document(uploaded_file)
#

# %% [markdown]
# ### Paso 5. Definimos nuestra función de generate_response
# - Hacemos uso de nuestra función `split_document`
# - Recuerda usar una temperatura de 0
# - Hacemos uso de [RetrievalQA](https://python.langchain.com/docs/use_cases/question_answering/vector_db_qa)
# - `RetrievalQA` también tiene las mismas opciones que load_summarize_chain (stuff, map_reduce y refine)
#
#

# %%
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA

def generate_response(uploaded_file, query_text):
  #Split the PDF file
  documents = split_document(uploaded_file)
  # Load OpenAI embeddings
  embeddings = OpenAIEmbeddings(temperature=0, openai_api_key=openai_api_key)
  # Create a vectorstore from documents
  db = Chroma.from_documents(documents, embeddings)
  # Create retriever interface
  retriever = db.as_retriever()
  # Create QA chain
  qa = RetrievalQA.from_chain_type(llm=OpenAI(openai_api_key=openai_api_key), chain_type='stuff', retriever=retriever)
  # qa= RetrievalQA | llm | retriever
  return qa.run(query_text)

# %% tags=["active-ipinb"]
# print(generate_response(uploaded_file, "Quienes son los personajes principales?"))

# %% [markdown]
# ## Paso 6. Creamos nuestra app en Streamlit usando la funcion generate_response (Es casi idéntica a la de st_tutorial_1)
#
# - crea un nuevo archivo app.py
# - nuestra app hará uso de las funciones de streamlit:
#   - [st.file_uploader](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)
#   - [st.title](https://docs.streamlit.io/library/api-reference/text/st.title)
#   - [st.form](https://docs.streamlit.io/library/api-reference/control-flow/st.form)
#   - [st.text_input](https://docs.streamlit.io/library/api-reference/widgets/st.text_input)
#   - [st.form_submit_button](https://docs.streamlit.io/library/api-reference/control-flow/st.form_submit_button)
#   - [st.info](https://docs.streamlit.io/library/api-reference/status/st.info)
#   - [st.warning](https://docs.streamlit.io/library/api-reference/status/st.warning)

# %% [markdown]
# ## Paso 7. Ejecuta la aplicación
# (También puedes ejecutarla ene una terminal aparte si así lo prefieres)

# %%
# !streamlit run app.py

# %% [markdown]
# ![Explanation](assets/image.png)
