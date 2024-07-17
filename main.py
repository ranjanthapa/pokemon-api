from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from configuration.database import get_db
from models.pokemon import Pokemon
from models.pokemon import Pokemon

app = FastAPI()


@app.get("/")
async def get_pokemon_list(
    name: str = None,
    pokemon_type: str = None,
    db: AsyncSession = Depends(get_db)
):
    try:
        query = select(Pokemon)

        if name:
            query = query.where(Pokemon.name == name)
        if pokemon_type:
            type_list = [pokemon_type]
            query = query.where(Pokemon.pokemon_type.any(type_list))
        result = await db.execute(query)
        pokemon_list = result.scalars().all()

        pokemon_data = [
            {"id": pokemon.id,"name": pokemon.name, "types": pokemon.pokemon_type, "image": pokemon.image} for pokemon in pokemon_list
        ]
        return {"results": pokemon_data}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch data: {str(e)}")
