# Building chatbot using paid LLM's and open source LLM

from langchain_openai import ChatOpenAI # Open AI API
from langchain_core.prompts import ChatPromptTemplate # Prompt template
from langchain_core.output_parsers import StrOutputParser # Default output parser whenever a LLM model gives any response
from langchain_community.llms import Ollama
from langchain_groq import ChatGroq
import streamlit as st # UI
import os
from dotenv import load_dotenv

load_dotenv()

# Langsmith tracking (Observable)
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
# os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
# os.environ["LANGCHAIN_TRACING_VR"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Defining Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","Act as a Chef"), # If user asked any other unrelated topics, it will not answer. It will respond accordingly.
        ("user","Question:{question}")
    ]
    )

# UI

st.title("Talk with the Chef ")
inputText = st.text_input("Ask questions about Dishes")

# Not having the open AI API key, but learning to create functionality
# Ollama enables us to run large language models locally, automatically does the compression

# llm = ChatOpenAI(model="llm")
# llm = Ollama(model="llama2") # Using ollama and llama2 model
# outputParser = StrOutputParser() 
# chain = prompt|llm|outputParser # Defining chain - Combining 


# Using groq inference engine

# groqllm = ChatGroq(model="llama3-70b-8192",temperature=0) 
groqApi = ChatGroq(model="gemma-7b-It",temperature=1)
outputparser = StrOutputParser()
chainSec = prompt|groqApi|outputparser

#  Langchain provides features that we can attach in the form of chain
#1 Prompt
#2 Integration with llm
#3 Output Parser

# if inputText:
#     st.write(chain.invoke({'question':inputText}))
    
    
if inputText:
    st.write(chainSec.invoke({'question':inputText}))