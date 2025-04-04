from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

#Allows frontend to access during dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

class NoteRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize_note(note: NoteRequest):
    #Temp dummy notes
    return {
        "Summary": f"Summary of: {note.text[:50]}..."
    }