# Simple python script to hit LLM models using langchain package

import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0, api_key=GEMINI_API_KEY, LANGSMITH_TRACING=True, LANGSMITH_API_KEY=os.getenv("LANGSMITH_API_KEY"))

result = llm.invoke("What is the capital of France?")
print(result.content)
result = llm.invoke("Where is it located?")
print(result.content)
print(result.usage_metadata)
print("*" * 100)
print(result)
