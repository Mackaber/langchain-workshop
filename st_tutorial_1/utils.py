# Inspired from [LangChain tutorial #1: Build an LLM-powered app in 18 lines of code
# ](https://blog.streamlit.io/langchain-tutorial-1-build-an-llm-powered-app-in-18-lines-of-code/)

# !pip install streamlit openai langchain 

global openai_api_key
openai_api_key="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"

# +
from langchain.llms import OpenAI

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  return llm(input_text)


# -

prompt = """
    Hola, como estas?
"""

print(generate_response(prompt))
