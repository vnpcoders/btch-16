import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMMathChain,LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import wikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool,initialize_agent
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
chain=LLMChain(llm=llm,prompt=prompt_template)

reasoning_tool=Tool(
    name="Resoning Tool",
    func= chain.run,
    description="A tool for answering logic-based and  reasoning question."

)

assistant_agent=initialize_agent(
tools=[wikipedia_Tool,calculator,reasoning_tool],
llm=llm,
agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
verbose=False,
handle_parsing_errors=True)

if "messages" not in st.session_state:
    st.session_state['messages']={
        'role':'assistant',
        'content':"Hi,I am a math chatbot powerd by gemini"
    }
for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

if st.button("Find answer"):
    if question:
        with st.spinner("Generation respones..."):
            st.session_state.messages.append
            ({'role':'assistant','content':question})
            st.chat_message("user").write(question)

            st_cb=StdOutCallbackHandler(st.container()
                                        ,expand_new_thoughts=False)
            response=assistant_agent.run(st.session_state.messages,collbacks=[st_cb])
            st.session_state.messages.app



