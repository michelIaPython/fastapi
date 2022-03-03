#Python
from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel
from pydantic import Field

# FastAPI
from fastapi import FastAPI, Path, Query, Body

app = FastAPI()

# Models

class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"

class Location(BaseModel):
    city: str
    state:str
    country: str

class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=2,
        max_length=30
        )
    last_name: str = Field(
        ...,
        min_length=2,
        max_length=30
        )
    age: int = Field(
        ...,
        gt=0,
        le=115
    )
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)

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
    name: Optional[str] = Query(
        None, 
        min_length=2, 
        max_length=30,
        tittle="Person Name",
        description="This is the person name. It's between 1 and 30 chracters"  
        ),
    age: str = Query(
        ...,
        title="Person Age",
        description="This is the person age. It's required"
        )
    
):
    return {name: age}

# Validaciones: Path Parameters
@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ..., 
        gt= 0,
        title="Person ID",
        description="This is the id's Person"
        )
):
    return {person_id: "it exist"}

# Validaciones: Request Body
@app.put("/person/{person_id}")
def update_peson(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt=0
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return person

# Validaciones: Models



