import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def getLlamaresponse(prompt,no_words,style):
    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    template="""
    Write a blog for {style} job profile for a topic {prompt} within {no_words} words 
    """
    prompttemplate=PromptTemplate(input_variables=['style','prompt','no_words'],
                                  template=template)
    response=llm(prompttemplate.format(style=style,prompt=prompt,no_words=no_words))
    print(response)
    return response

st.set_page_config(page_title='Generate Blogs',
                   layout='centered',
                   initial_sidebar_state='collapsed')
st.header("Generate Blogs")

input_text=st.text_input('Enter the blog prompt')

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of words')
with col2:
    blog_style=st.selectbox('Select blog style',('Research','Data Scientists','Regular people'),index=0)
submit=st.button("Generate")
if submit:
    st.write(getLlamaresponse(input_text,no_words,blog_style))