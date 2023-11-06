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
# (Inspirado en [LangChain tutorial #4: Build an Ask the Doc app](https://blog.streamlit.io/langchain-tutorial-4-build-an-ask-the-doc-app/))

# %% [markdown]
# # Platica con tus documentos
# ### Documents

# %% [markdown]
# <span style="color:red;">IMPORTANTE: Nunca subas código a github con llaves privadas!</span>

# %%
openai_api_key="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"

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

# %%
# %pip install pypdf chromadb tiktoken

# %%
# %pip install ipywidgets streamlit openai langchain

# %% tags=["active-ipynb"]
# from ipywidgets import FileUpload
# from IPython.display import display
# uploader = FileUpload()
# display(uploader)

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


# %% tags=["active-ipynb"]
# uploaded_file = uploader.value[0].content.tobytes()
# split_document(uploaded_file)
#

# %%
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
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
  return qa.run(query_text)

# %% tags=["active-ipinb"]
# print(generate_response(uploaded_file, "Quienes son los personajes principales?"))

# %%
# !streamlit run app.py
