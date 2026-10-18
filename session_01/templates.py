
import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# llm = ChatOpenAI(model="gpt-5.4-mini", temperature=0, api_key=API_KEY)
llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0, api_key=GEMINI_API_KEY)

template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that answers every question with a joke."),
    ("human", "Question: {prompt}"),
])

prompt = template.invoke({"prompt": "What is the capital of France?"})
print(prompt)
result = llm.invoke(prompt)
print(result.content)