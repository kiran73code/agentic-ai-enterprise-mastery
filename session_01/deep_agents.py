import os

from deepagents import create_deep_agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash", temperature=0, api_key=GEMINI_API_KEY
)


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_deep_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
print(
    agent.invoke(
        {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
    )
)
