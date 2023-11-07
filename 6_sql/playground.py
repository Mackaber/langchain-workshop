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

# %%
# !pip install psycopg2

# %%
from langchain.utilities import SQLDatabase

db = SQLDatabase.from_uri("postgresql://Mackaber:G5PyrWgnhdE1@ep-rough-violet-21813379.us-east-2.aws.neon.tech/chinook")

#

import pandas as pd
result = db.run('SELECT * FROM "Album";')


# %%
result

# %%
import ast
pd.DataFrame(ast.literal_eval(result))


# %%
def get_schema(_):
  return db.get_table_info()


# %%
from langchain.prompts import ChatPromptTemplate

template = """Based on the table schema below, write a SQL query that would answer the user's question:
{schema}

Notice, this is for a {engine} Database, I'ts very important to use it's specific syntax. 
Keep in mind the use of quotes and case-sensitive details for {engine}.

Question: {question}
SQL Query:"""


# %%
def get_engine(_):
  return "Postgresql"


# %%
prompt = ChatPromptTemplate.from_template(template)

# %%
from langchain.chat_models import ChatOpenAI
model = ChatOpenAI(openai_api_key="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")

# %%
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

def generate_sql_query(_):
  passthrough = RunnablePassthrough.assign(schema=get_schema, engine=get_engine)
  sql_response = passthrough| prompt | model.bind(stop=["\nSQLResult:"]) | StrOutputParser()
  return sql_response



# %%
generate_sql_query().invoke({"question": "How many employees are there?"})

# %%
template_response = """Based on the table schema below, question, sql query, and sql response, write a natural language response:
{schema}

Question: {question}
SQL Query: {query}
SQL Response: {response}"""
prompt_response = ChatPromptTemplate.from_template(template_response)

# %%
from langchain.chat_models import ChatOpenAI
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough as pt

def generate_response(input):
  chain = (
          pt.assign(query=generate_sql_query) 
        | pt.assign(schema=get_schema)
        | pt.assign(response=lambda x: db.run(x["query"]))
        | pt.assign(engine=get_engine) 
        | prompt_response 
        | model
  )
  return chain.invoke({"question": input})



# %%
generate_response("Which album has the longest name?")
