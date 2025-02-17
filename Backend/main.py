import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

class User(BaseModel):
    name: str

class Person(BaseModel):
    person: List[User]


app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

memory_db = {"person": []}

@app.get("/person", response_model=Person)
def get_person():
    return Person(person=memory_db["person"])

@app.post("/person", response_model=User)
def add_person(user: User):
    memory_db["person"].append(user)
    return user

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)