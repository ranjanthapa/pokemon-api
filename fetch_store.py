import asyncio
import aiohttp
from sqlalchemy.ext.asyncio import AsyncSession
from configuration.database import engine, Base
from models.pokemon import Pokemon

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon"

async def fetch_pokemon_data(session) -> list:
    results = []
    async with session.get(POKEAPI_URL) as response:
        if response.status != 200:
            raise Exception(f"Failed to fetch data: {response.status}")
        pokemon_data = await response.json()
        for data in pokemon_data['results']:
            async with session.get(data['url']) as detail_response:
                if detail_response.status != 200:
                    raise Exception(f"Failed to fetch detail data: {detail_response.status}")
                detail_data = await detail_response.json()
                temp_data = {
                    'name': detail_data['name'],
                    'image': detail_data['sprites']['front_default'],
                    'types': [_type['type']['name'] for _type in detail_data['types']]
                }
                results.append(temp_data)
    return results

async def store_pokemon_data(pokemon_list, db: AsyncSession):
    for pokemon_data in pokemon_list:
        pokemon = Pokemon(
            name=pokemon_data['name'],
            image=pokemon_data['image'],
            pokemon_type=pokemon_data['types']
        )
        db.add(pokemon)
    await db.commit()

async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async with aiohttp.ClientSession() as http_session:
        pokemon_list = await fetch_pokemon_data(http_session)
    
        async with AsyncSession(engine) as session:
            await store_pokemon_data(pokemon_list, session)

if __name__ == "__main__":
    asyncio.run(main())
