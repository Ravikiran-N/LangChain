from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] =os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] =os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

##Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant, provide responses to questions"),
        ("user","Question:{question}")
    ]
)

## Stremlit framework
st.title("Langchain demo with OPEN AI")
input_text = st.text_input("Search the topic you want")

##OpenAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")
Output_parser = StrOutputParser()
chain = prompt|llm|Output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))

