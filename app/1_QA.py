import os
from dotenv import load_dotenv

from langchain_cohere import CohereEmbeddings

from langchain_openai import ChatOpenAI
load_dotenv()
# embeddings = CohereEmbeddings(
#     model="embed-english-light-v3.0",
#     cohere_api_key=os.getenv("COHERE_API_KEY"),
# )
llm = ChatOpenAI( api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
    model="openai/gpt-oss-120b",
    
)

while True:
    query= input("user: ")
    res=llm.invoke(query)
    print("AI:",res.content)
    if query.lower() in ["quit","exit","bye"]:
        print("Good Bye")
        break



