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
# (Inspirado en [Adding memory](https://python.langchain.com/docs/expression_language/cookbook/memory))

# %% [markdown]
# # Un chat que recuerda
# ### Memory

# %%
openai_api_key="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"

# %%
from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory(return_messages=True)

# %%
memory.load_memory_variables({})

# %%
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful chatbot"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

# %%
prompt

# %%
from operator import itemgetter
from langchain.chat_models import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda

def generate_response(input):
  model = ChatOpenAI(openai_api_key=openai_api_key)
  passthrough = RunnablePassthrough.assign(history=RunnableLambda(memory.load_memory_variables) | itemgetter("history"))
  chain = passthrough | prompt | model
  inputs = {"input": input}
  response = chain.invoke(inputs)
  memory.save_context(inputs, {"output": response.content})
  return response.content


# %%
generate_response("Hola mi nombre es mackaber")

# %%
generate_response("Como me llamo?")

# %%
