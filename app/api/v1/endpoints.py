import requests
from fastapi import APIRouter, HTTPException

router = APIRouter()

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon"

@router.get("/fetch_pokemon/{name}")
async def fetch_pokemon(name: str):
    response = requests.get(f"{POKEAPI_URL}/{name}")
    if response.status_code == 200:
        data = response.json()
        pokemon_info = {
            "name": data["name"],
            "image": data["sprites"]["front_default"],
            "types": [type_info["type"]["name"] for type_info in data["types"]]
        }
        return pokemon_info
    else:
        raise HTTPException(status_code=response.status_code, detail="Pokemon not found")
