# MCP Client ko multiple MCP Servers se connect karne ke liye
from langchain_mcp_adapters.client import MultiServerMCPClient

# LangChain Agent create karne ke liye
from langgraph.prebuilt import create_react_agent

# Groq LLM import karna
from langchain_groq import ChatGroq

# .env file se API keys load karna
from dotenv import load_dotenv
load_dotenv()

# Asynchronous programming ke liye
import asyncio


# Main asynchronous function
async def main():

    # Multiple MCP Servers ka configuration
    client = MultiServerMCPClient(
        {
            # Math MCP Server configuration
            "math": {
                "command": "python",  # Python interpreter se server start karna
                "args": ["mathserver.py"],  # Math server ki file
                "transport": "stdio",  # STDIO communication use karna
            },

            # Weather MCP Server configuration
            "weather": {
                "url": "http://localhost:8000/mcp",  # Weather Server ka MCP endpoint
                "transport": "streamable_http",  # HTTP communication use karna
            }
        }
    )

    # Connected MCP Servers ke saare tools load karna
    tools = await client.get_tools()

    # Groq LLM initialize karna
    model = ChatGroq(model="openai/gpt-oss-120b")

    # LLM + MCP Tools ko combine karke Agent banana
    agent = create_react_agent(model, tools)

    # Agent ko user ka question dena aur response ka wait karna
    math_response = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What's (3 + 5) x 12?"
                }
            ]
        }
    )

    # Agent ke last message ka content print karna
    print("Math response:", math_response["messages"][-1].content)


# asyncio ko import kiya tha, isliye asyncio.run() use kiya
# main() asynchronous function ko execute karna
asyncio.run(main())