import os

from dotenv import load_dotenv

from langchain_cohere import CohereEmbeddings

from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.vectorstores import InMemoryVectorStore

# load .env step 1
load_dotenv()
#load for embeddings
embeddings = CohereEmbeddings(
    model="embed-english-light-v3.0",
    cohere_api_key=os.getenv("COHERE_API_KEY"),
)
#load for llm
llm = ChatOpenAI( api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
    model="openai/gpt-oss-120b",
    
)
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a translator. Translate the input into {language}."),
    ("user", "{query}")
])

# Connect the template and LLM into a chain
chain = prompt_template | llm

# Invoke the chain with a dictionary
# res = prompt_template.invoke({"language": "Punjabi", "query": "I love Javascript"})
res = chain.invoke({"language": "Punjabi", "query": "I love everybody"})
print(res.content)

#chains which are runnable

# print(res.content)

