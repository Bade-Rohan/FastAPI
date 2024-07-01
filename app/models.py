from pydantic import BaseModel, HttpUrl

class Pokemons(BaseModel):
    name:str
    url:str
   
   