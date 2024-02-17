import os
from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

def getresponse(question):
    llm=OpenAI(temperature=0.7)
    response=llm(question)
    return response
    
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain App")

input=st.text_input("Input: ",key="input")
response=getresponse(input)
submit=st.button("Ask a question")

if submit:
    st.subheader("Response from LLM is:")
    st.write(response)
