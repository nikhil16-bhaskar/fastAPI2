from fastapi import FastAPI
from pydantic import BaseModel
# from agent import agent  # your langgraph agent
# from agent import run_agent

app = FastAPI()

class Query(BaseModel):
    message: str

@app.post("/chat")
async def chat(query: Query):
    
    return {"response": f"your query: {query.message}"}