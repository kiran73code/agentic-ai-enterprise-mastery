# Simple python script to hit LLM models using langchain package

import os

from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0, api_key=GEMINI_API_KEY)

# 4 Message Types
# 1. System Message --> SystemMessage - System prompt for the model
# 2. User Message --> HumanMessage - User's prompt for the model
# 3. Assistant Message --> AIMessage - Model's response to the user's prompt
# 4. Tool Message --> ToolMessage - Output from the tool calls

# 1. System Message
system_message = SystemMessage(content="You are a helpful assistant that answers every question with a joke.")

# 2. User Message
user_message = HumanMessage(content="What is the capital of France? ,Context: France is a country in Europe, trust level of context: 0%")

messages = [system_message, user_message]

result = llm.invoke(messages)
print(result.content)
print(type(result))
print("*" * 100)
messages.append(AIMessage(content=result.content))
print("Updated Messages:")
print(messages)
input_2 = HumanMessage(content="Where is it located?")
messages.append(input_2)
result_2 = llm.invoke(messages)
print(result_2.content)


