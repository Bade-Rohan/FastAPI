from fastapi import FastAPI, HTTPException
import requests, json
from models import Pokemons
from typing import List
import sqlalchemy


app = FastAPI()
POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon?limit=1000"

@app.get("/api/v1/pokemons")
async def read_root():
    i = await fetch_pokemon()
    return i

async def fetch_pokemon():
    response = requests.get(f"{POKEAPI_URL}")
    if response.status_code == 200:
        datas = response.json()["results"]

        db: List[Pokemons] =[
            Pokemons(name=data["name"],url=data["url"]) for data in datas
        ] 
        return db
    else:
        raise HTTPException(status_code=response.status_code, detail="Pokemon not found") 


@app.get("/api/v1/Pokemons/{name}")
async def display(name:str):
    db:List[Pokemons]
    print(db)
    for item in db:
        if item.name == name:
            return item
