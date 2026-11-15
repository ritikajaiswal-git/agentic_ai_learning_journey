MCP (Model Context Protocol) – Summary Notes
MCP is an open standard that allows AI applications to connect with external tools, data, and services in a common way.
1. Normal LangGraph Tool Calling
- We define tools inside our Python project using @tool.
- Store multiple tools in a list: tools = [add, multiply].
- Pass these tools to the LangGraph agent.
- The agent directly uses these tools.
- No separate MCP server or client is required.
2. MCP Tool Calling
MCP follows a Client-Server architecture.
- MCP Server: Provides tools using @mcp.tool().
- MCP Client: Connects to the MCP server and discovers available tools.
- LangGraph Agent: Receives those tools through the MCP client and uses them.
Flow:
MCP Server
    ↓
MCP Client
    ↓
get_tools()
    ↓
LangGraph Agent
    ↓
Uses the required tool


3. Difference Between @tool and @mcp.tool()
@tool	@mcp.tool()
Creates a LangChain tool	Registers a tool on an MCP server
Directly used in LangChain/LangGraph	Accessed through an MCP client
Mostly app-specific integration	Can be reused by multiple MCP-compatible applications

4. Why Do We Need MCP?
Suppose we create a Math Server with two tools:
- add()
- multiply()
We can connect this same server to:
- LangGraph Agent
- Claude Desktop
- Other MCP-compatible applications
We don't need to define the same tools separately in every application.
5. Is a Separate MCP Server Compulsory?
No.
- If tools are only needed in your LangGraph project, normal @tool is sufficient.
- If you want to expose and reuse tools across multiple AI applications, MCP is useful.
6. Relationship Between LangChain, LangGraph, RAG and MCP
Technology	Main purpose
LangChain	Building applications using LLMs, prompts, tools, etc.
LangGraph	Managing agent workflows and tool-calling loops
RAG	Retrieving relevant information from external knowledge sources
MCP	Standardized communication between AI applications and external tools/data

Remember: MCP does not replace LangChain or LangGraph. It provides a standardized way for them to connect with external tools and services.



uv init k bd uv venv
# MCP (Model Context Protocol)

MCP is an open standard that allows AI applications to connect with external tools, data and services.
1. Main Components of MCP
1. MCP Server
- Provides tools, resources and prompts.
- One server can have multiple tools.
- Example: Math server (add(), divide()).
2. MCP Client
- Connects to MCP Server.
- Maintains connection and accesses available tools.
3. Host Application
- Main AI application.
- Uses tools through the MCP Client.
- Example: Claude Desktop, LangGraph Agent.
2. Working of MCP
1. Server → Provides tools.
2. Client → Connects to server.
3. Host → Uses tools through client.
4. Server executes the request and returns the result. ye v likh do
Building MCP Server & MCP Client
We are going to build MCP Server and MCP Client and integrate them with a LangGraph Agent.

1. What are we going to create?
MCP Server: Provides tools like addition, multiplication and Weather API.

MCP Client: Connects to MCP Server and accesses its tools.

LangGraph Agent: Uses MCP tools through the MCP Client.

2. MCP Workflow
User gives input to the chatbot.

LLM understands the user's request.

MCP Client connects to MCP Server using MCP Protocol.

MCP Server provides the required tools.

Tool executes the request.

Result returns to the chatbot through MCP Client.

LLM generates the final response.

3. Transport Mechanisms
Transport defines how MCP Client and MCP Server communicate.

stdio: Communication through standard input/output, generally for local servers.

HTTP (Streamable HTTP): Communication over HTTP, useful for remote servers.



note
mathserver.py is mcp server hi
weather.py  v
# STDIO vs HTTP Transport

# STDIO:
# Local communication between MCP Client and MCP Server.
# stdin se request receive hoti hai aur stdout se response send hota hai.
# MCP Client server process ko start karta hai.
# Generally local tools ke liye use hota hai.
# Isme HTTP server ya API endpoint create nahi hota.
# Terminal mein run karne par HTTP API service provide nahi hoti.


# HTTP (Streamable HTTP):
# Local ya remote network communication ke liye use hota hai.
# HTTP requests aur responses ke through communication hota hai.
# Server HTTP endpoint par run hota hai.
# Client HTTP ke through server se connect karta hai.
# Remote services aur applications ke liye useful hai.
# Terminal mein server run karne par HTTP endpoint/API service available hoti hai.
# Iske liye HTTP server required hota hai.

client.py should interact with both weather.py and math.py 
