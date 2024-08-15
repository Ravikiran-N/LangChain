from fastapi import FastAPI
from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
#from langchain.schema.runnable import RunnableMap
from langserve import add_routes
from langchain_core.runnables.schema import StreamEvent
from langserve.api_handler import APIHandler
from langsmith.schemas import FeedbackIngestToken
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

#FastAPI

app=FastAPI(
    title ="Langchain Server",
    version ='1.0',
    description="A simple API"
)

add_routes(
    app,
    ChatOpenAI(),
    path='/openai'
)
model=ChatOpenAI()

##Ollama 
llm=Ollama(model="llama2")

##Prompt templates
prompt1 = ChatPromptTemplate.from_template("Write an essay about {topic} with 100 words")
prompt2= ChatPromptTemplate.from_template("Write me a poem about {topic} with 100 words")

add_routes(
    app,
    prompt1|model,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__== "__main__":
    uvicorn.run(app,host="localhost",port=8000)

