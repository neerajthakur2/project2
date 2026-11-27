import streamlit as st
import os
from dotenv import load_dotenv

from langchain_cohere import CohereEmbeddings

from langchain_openai import ChatOpenAI
load_dotenv()

llm = ChatOpenAI( api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
    model="openai/gpt-oss-120b",
    
)




st.title("AskBuddy🤣 Ask Neeraj")
st.markdown("My QnA with langchain")
query=st.chat_input("Ask Question ?")
if "messages" not in st.session_state:
    st.session_state.messages=[]
for message in st.session_state.messages:
    role=message["role"]
    content=message["content"]
    st.chat_message(role).markdown(content)
#this is comment
if query:
    st.session_state.messages.append({
        "role":"user",
        "content":"query"
    })
    print(query)
    st.chat_message("user").markdown(query)
    res=llm.invoke(query)
    st.chat_message("ai").markdown(res.content)
    st.session_state.messages.append({
            "role":"Neeraj",
            "content":res.content
        })