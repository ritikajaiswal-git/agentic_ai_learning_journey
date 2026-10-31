from mcp.server.fastmcp import FastMCP
mcp=FastMCP("Math")#math is a tool name

@mcp.tool()
def add(a:int,b:int)->int:
    #docsttring is porvided for llm to understand the function nd then match  with prompt
    """
    _summary_
    Add two number 
    """
    return a+b

@mcp.tool()
def multiple(a:int,b:int)->int:
    """Multiply two number"""
    return a*b

# Check whether this file is running directly
if __name__ == "__main__":


    # Start MCP Server using stdio transport
    mcp.run(transport="stdio")
     # transport="stdio" argument server ko batata hai ki:

# Standard input/output (stdin aur stdout) ka use karke
# tool function calls ko receive aur unka response dena hai.

# FastMCP ka use karke MCP Server create karna
# FastMCP("Math") → Math naam ka MCP Server banaya

# @mcp.tool() → Python functions ko MCP Tools mein convert karna

# add() → Do numbers ko add karne wala tool

# multiple() → Do numbers ko multiply karne wala tool

# Docstring → Tool ka description batata hai, jisse LLM ko tool ka purpose samajh aata hai

# mcp.run(transport="stdio") → STDIO transport ke through MCP Server start karna

# __main__ → Check karta hai ki file directly run ho rahi hai ya nahi

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