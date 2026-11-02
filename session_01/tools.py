from deepagents import create_deep_agent
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

load_dotenv()


class AddInput(BaseModel):
    a: int = Field(description="First number - integer")
    b: int = Field(description="Second number - integer")


@tool
def add(a: int, b: int) -> int:
    """Add two numbers together
    Args:
        a: First number - integer
        b: Second number - integer
    Returns:
        The sum of the two numbers
    """
    return a + b


print(add.invoke(input={"a": 1, "b": 2}))  # input is a dictionary


@tool(args_schema=AddInput)
def add_with_schema(a: int, b: int) -> int:
    """Add two numbers together
    Args:
        a: First number - integer
        b: Second number - integer
    Returns:
        The sum of the two numbers
    """
    return a + b


@tool
def get_weather(city: str) -> str:
    """Get the weather of a city
    Args:
        city: The city to get the weather of
    Returns:
        The weather of the city
    """
    return f"The weather of {city} is sunny"


print(add_with_schema.invoke(input={"a": "1.0", "b": "5.0"}))  # input is a dictionary

llm = ChatOpenAI(model="gpt-5.4-mini", temperature=0).bind_tools([add, get_weather])

messages = [HumanMessage(content="What is 2 + 3 , and the weather in Tokyo?")]
result = llm.invoke(messages)
print("*********")
print(result)
print("*********")
messages.append(result)

print(f"Output for first message is {result}")

tool_names = {
    "add": add,
    "add_with_schema": add_with_schema,
    "get_weather": get_weather,
}

for call in result.tool_calls:
    print(f"Tool call name: {call["name"]}")
    print(f"Tool call arguments: {call["args"]}")
    tool_result = tool_names[call["name"]].invoke(call["args"])
    print(f"Tool result: {tool_result}")
    messages.append(ToolMessage(content=tool_result, tool_call_id=call["id"]))

final_result = llm.invoke(messages)
print(f"Final result: {final_result}")
print("*" * 100)
agent = create_deep_agent(
    model="openai:gpt-5.5",
    tools=[add, get_weather],
    system_prompt="You are a helpful assistant",
)

print(
    agent.invoke(
        {
            "messages": [
                {"role": "user", "content": "What is 2 + 3 , and the weather in Tokyo?"}
            ]
        }
    )
)
print("*" * 100)
