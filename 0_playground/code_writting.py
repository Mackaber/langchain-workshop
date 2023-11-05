# %pip install langchain-experimental

from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema.output_parser import StrOutputParser
from langchain_experimental.utilities import PythonREPL
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from operator import itemgetter
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

filename="oscars.csv"

headers="oscar_no,oscar_yr,award,name,movie,age,birth_pl,birth_date,birth_mo,birth_d,birth_y"

db_template = f"""Yoy are given a database in csv named: {filename} with the headers: {headers}
"""

code_template = """Given the previous CSV database write some python code to solve the user's problem. 

Return only python code in Markdown format, e.g.:

```python
....
```"""

model = ChatOpenAI(openai_api_key="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")

db_template

#prompt = ChatPromptTemplate.from_messages([("system", template), ("human", "{input}")])
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", db_template),
        ("system", code_template),
        #MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

memory = ConversationBufferMemory(memory_key="chat_history")


def _sanitize_output(text: str):
    _, after = text.split("```python")
    return after.split("```")[0]


itemgetter('thing')

itemgetter('bs')({"bs": "x"})

chain =  prompt | model | StrOutputParser() | _sanitize_output | PythonREPL().run


chain

inputs = {"input": "Which birth place is the most common among the winners?"}
response = chain.invoke(inputs)
response

memory = ConversationBufferMemory(return_messages=True)
memory.load_memory_variables({})

inputs = {"input": "Read oscars.csv what is its last entry?"}
response = chain.invoke(inputs)
response

memory.save_context(inputs, {"output": response.content})

memory.load_memory_variables({})

chain

inputs = {"input": "What does the code you suggested me do?"}
chain.invoke(inputs)

chain

# +
import pandas as pd
import plotly.express as px

# Read the csv file into a pandas DataFrame
df = pd.read_csv('oscars.csv')

# Count the frequency of each birth place
birth_place_counts = df['birth_pl'].value_counts().reset_index()

# Rename the columns
birth_place_counts.columns = ['Birth Place', 'Count']

# Sort the DataFrame by count in descending order
birth_place_counts = birth_place_counts.sort_values(by='Count', ascending=False)

# Create a bar plot using plotly
fig = px.bar(birth_place_counts, x='Birth Place', y='Count', title='Most Frequent Birth Places')
fig.show()
# -


