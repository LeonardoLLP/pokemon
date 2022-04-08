from pokemon import Pokemon
from pokemon_water import PokemonWater
from pokemon_air import PokemonAir
from pokemon_earth import PokemonEarth
from pokemon_electricity import PokemonElectricity

import pandas as pd



filepath_c1 = "coach_1_pokemons.csv"
filepath_c2 = "coach_2_pokemons.csv"

c1_df = pd.DataFrame(filepath_c1, sep=",")
c2_df = pd.DataFrame(filepath_c2, sep=",")

def get_data_from_user(data: pd.DataFrame):
    
