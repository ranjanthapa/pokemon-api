# Pokemon API Project

This project is a FastAPI application that fetches Pokémon data from the PokeAPI and stores it in a PostgreSQL database. It provides an API to query the stored data based on Pokémon name and type.

## Features

- Fetch Pokémon data from the PokeAPI.
- Store Pokémon data in a PostgreSQL database.
- Retrieve a list of Pokémon with their name, type, and image.
- Filter Pokémon by name and type.

## Requirements

- Python 3.11+
- PostgreSQL
- FastAPI
- SQLAlchemy
- aiohttp

# API Documentation

## Base URL

http://127.0.0.1:8000/

## Endpoints

### Get Pokémon List

Retrieve a list of Pokémon with their name, type, and image. You can filter the Pokémon by name and type.

- **URL:** `/`
- **Method:** `GET`
- **Query Parameters:**

  - `name` (optional): Filter by Pokémon name.
  - `pokemon_type` (optional): Filter by Pokémon type.

- **Response:**

  - `200 OK`: Successfully retrieved the list of Pokémon.
  - `500 Internal Server Error`: Failed to fetch data.

- **Example Request:**

  ```bash
  curl -X GET "http://127.0.0.1:8000/?pokemon_type=poison&name=ivysaur"
  ```

- **Output:**
  ```json
  {
    "results": [
      {
        "id": 2,
        "name": "ivysaur",
        "types": ["grass", "poison"],
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/2.png"
      }
    ]
  }
  ```
