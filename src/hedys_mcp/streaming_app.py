
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.hedys_mcp import server
import asyncio

app = FastAPI(title="Hedy's MCP Streaming Server")

@app.get("/joke")
async def get_deborahs_joke():
    # Call the deborahs_jokes tool asynchronously
    result = await server.handle_call_tool("deborahs_jokes", {})
    # Return the joke text
    return {"joke": result[0].text}

class NoteIn(BaseModel):
    name: str
    content: str

class NoteUpdate(BaseModel):
    name: str
    new_content: str

@app.get("/notes")
def list_notes():
    return list(server.notes.keys())

@app.get("/notes/{name}")
def get_note(name: str):
    if name not in server.notes:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"name": name, "content": server.notes[name]}

@app.post("/notes")
def add_note(note: NoteIn):
    server.notes[note.name] = note.content
    return {"status": "added", "note": note.name}

@app.put("/notes")
def update_note(note: NoteUpdate):
    if note.name not in server.notes:
        raise HTTPException(status_code=404, detail="Note not found")
    server.notes[note.name] = note.new_content
    return {"status": "updated", "note": note.name}

@app.delete("/notes/{name}")
def delete_note(name: str):
    if name not in server.notes:
        raise HTTPException(status_code=404, detail="Note not found")
    del server.notes[name]
    return {"status": "deleted", "note": name}
