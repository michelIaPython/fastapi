#Python
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI, Query, Body

app = FastAPI()

# Models

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

@app.get("/")
def home():
    return {"Hello":"World"}

# Request and Response body

@app.post("/person/new")
                                   # Obliga a que el parametro person en el request body sea obligatorio
def create_person(person: Person = Body(...)):
    return person

#Validaciones: Query PArameters

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None, min_length=2, max_length=30),
    age: str = Query(...)
    
):
    return {name: age}









