# ---
# jupyter:
#   jupytext:
#     custom_cell_magics: kql
#     formats: ipynb,py:percent
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
# Inspired from [LangChain tutorial #1: Build an LLM-powered app in 18 lines of code](https://blog.streamlit.io/langchain-tutorial-1-build-an-llm-powered-app-in-18-lines-of-code/)

# %%
# %pip install streamlit openai langchain 

# %%
global openai_api_key
openai_api_key="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"

# %%
from langchain.llms import OpenAI

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  return llm(input_text)


# %%
prompt = """
    Hola, como estas?
"""

# %% tags=["active-ipynb"]
# print(generate_response(prompt))
