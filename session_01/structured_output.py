
import os
from typing import TypedDict

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


class AnswerWithJustifcation(BaseModel):
    answer: str = Field(description="The answer to the question")
    justification: str = Field(description="Why this answer is correct")


llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash", 
            temperature=0, api_key=GEMINI_API_KEY).with_structured_output(AnswerWithJustifcation)

result = llm.invoke("What is 2* 3 ?")
print(result)
print(result.model_dump_json())


class AnswerWithJustifcation(TypedDict): # generally used to create/define a schema for the output or input
    answer: str
    justification: str
    

llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash", 
            temperature=0, api_key=GEMINI_API_KEY).with_structured_output(AnswerWithJustifcation)

result = llm.invoke("What is 2* 3 ?")
print(result)
print(result.model_dump_json())