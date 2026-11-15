#- mcp → Python ka MCP package.
#- server → Is package ka server-related module.
#- fastmcp → MCP server easily create karne ka interface.
#- FastMCP → Server create karne wali class.
#Hum FastMCP import kyun kar rahe hain?

#Taaki hum easily apna MCP server bana sakein aur usme tools register kar sakein.


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
#Ye Python ka concept hai.

#Python mein jab hum koi file run karte hain, toh us file ka special variable __name__ hota hai.

#Agar file directly run ho rahi hai, toh:
#__name__ == "__main__"



#True hota hai.
if __name__ == "__main__":


    # Start MCP Server using stdio transport
    mcp.run(transport="stdio") #mcp server strt hora h, cleint ar server k bich conversation stdio k through hogi
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

# Final difference
# Situation	__name__	mcp.run()
# python mathserver.py	"__main__"	Execute hoga
# import mathserver	"mathserver"	Execute nahi hoga
# Client config se python mathserver.py	"__main__"	Execute hoga

# Yaad rakhna: Tumhare project mein client.py server ko import nahi karta, balki command aur args ki help se alag process mein run karta hai.
