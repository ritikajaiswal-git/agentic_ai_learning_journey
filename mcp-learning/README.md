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
