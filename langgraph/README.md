uv init Python mein ek new project initialize karne ke liye use hota hai. Ye uv tool ka command hai, jo Python project setup aur dependency management ko fast banata hai.
 

 requirement.txt file bnane s jo v library install krna h wo dikhega

 uv venv s virtual environment dikhta
 activate krne k liye print activate k path in command prompt

 uv add -r requirements.txt
 
 01- 1. Content of the image
LangGraph Crash Course
Goal: Build a basic chatbot

Components of LangGraph
1. Edges
2. Nodes
3. State
Input → LLM → Content Generation

YouTube videos → Blog

Workflow
1. YouTube videos → Transcript
2. Transcript → Title
3. Title + Transcript → Content

2. How your workflow will work
YouTube Video URL

Node 1: Get Transcript

Extract video transcript

Node 2: Generate Title

LLM creates a suitable blog title

Node 3: Generate Blog

Use title + transcript to write the blog

Final Blog Output


3. Where LangGraph fits in
- State: Stores the transcript, generated title, and blog content.
- Nodes: Functions that extract the transcript and call the LLM.
- Edges: Define the order in which those functions execute.
- LLM: Generates the title and blog using a model provider