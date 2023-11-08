from langchain.llms.openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os


def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"),model_name="text-davinci-003",temperature=0.5)
    response =llm(question)
    return response


#initialze streamlit app

st.set_page_config(page_title="Q&Ademo")

st.header("langchain application demo")


# get user input
input = st.text_input("input: ", key="input")
response= get_openai_response(input)

submit= st.button("Ask the question")

# if ask buttom is clicked

if submit:
    st.subheader("the response is :")
    st.write(response)
    

