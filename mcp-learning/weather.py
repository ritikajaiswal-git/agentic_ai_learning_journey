# FastMCP import karna, MCP Server create karne ke liye
from mcp.server.fastmcp import FastMCP

# Weather naam ka MCP Server create karna
mcp = FastMCP("Weather")


# Python function ko MCP Tool banana
@mcp.tool()
async def get_weather(location: str) -> str:

    # Tool ka description: Given location ka weather batana
    """Get the weather location."""

    # Weather information return karna
    return "It's always raining in California"


# Check karna ki file directly run ho rahi hai ya nahi
if __name__ == "__main__":

    # Streamable HTTP transport ke through MCP Server start karna
    mcp.run(transport="streamable-http")
    #it run as a api service itself when u go to terminal and write python weather.py