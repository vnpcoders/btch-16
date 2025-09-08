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

llm= ChatGoogleGenerativeAI(model="gemini-2")
