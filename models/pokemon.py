from sqlalchemy import Column, Text, String, Integer, ARRAY
from configuration.database import Base

class Pokemon(Base):
    __tablename__ = "pokemons"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    pokemon_type = Column(ARRAY(String))
    image = Column(Text)


