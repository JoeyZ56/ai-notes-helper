from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


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