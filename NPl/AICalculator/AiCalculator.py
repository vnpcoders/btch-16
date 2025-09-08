import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMMathChain,LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import wikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StdOutCallbackHandler

st.set_page_config(page_title="Text to Math Problem Solver")
st.title("Text to Math problem Solver using Gemini")

#Gemini ApI Key
gemini_api_key= st.sidebar.text_input(Label="Google Gemini API key",type='password')
if  not gemini_api_key:
    st.info("Please add your gemini API Key to Continue")
    st.stop()

llm= ChatGoogleGenerativeAI(model="gemini-2.5-flash",
                            google_api_key=gemini_api_key)

wikipedia_wrapper=wikipediaAPIWrapper()
wikipedia_Tool=Tool(name="Wikipedia",func=wikipedia_wrapper,description="A tool for searching the Internet to find information on various object")

#math tool

math_chain=LLMMathChain.from_llm(llm=llm)
calculator=Tool(
    name="Calculator",
    func=math_chain.run,
    description="A tool For answering math related questions"
)

prompt="""
                  you are my personel agent task with solving users mathamatical questions
Question=st.text_input("question")
Answer:
"""
question=st.text_input("Enter your problem here")
prompt_template=PromptTemplate(input_variables=['question'],template=prompt)
