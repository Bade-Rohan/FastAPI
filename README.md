# Pokemon API

## Overview

This project is a simple FastAPI application that fetches and returns specific Pokémon data (name, image, and types) from a local JSON file.

## Project Structure
pokemon_api/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── models.py
│ ├── api/
│ │ ├── init.py
│ │ ├── v1/
│ │ │ ├── init.py
│ │ │ ├── endpoints.py
├── pokemon_data.json
├── requirements.txt
├── README.md


## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/Bade-Rohan/FastAPI.git
cd pokemon_api

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

uvicorn app.main:app --reload

http://127.0.0.1:8000/docs

[
    {
        "name": "pikachu",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
        "types": ["electric"]
    },
    {
        "name": "bulbasaur",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png",
        "types": ["grass", "poison"]
    },
    {
        "name": "charmander",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png",
        "types": ["fire"]
    },
    {
        "name": "squirtle",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png",
        "types": ["water"]
    }
]
