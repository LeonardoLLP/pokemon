from pokemon import Pokemon
from pokemon_water import PokemonWater
from pokemon_air import PokemonAir
from pokemon_earth import PokemonEarth
from pokemon_electricity import PokemonElectricity

import pandas as pd

filepath_c1 = "coach_1_pokemons.csv"
filepath_c2 = "coach_2_pokemons.csv"


headers = ["ID", "Name", "Move", "hp", "Attack", "Defense"]

c1_df = pd.read_csv(filepath_c1, sep=",", names=headers)
c2_df = pd.read_csv(filepath_c2, sep=",", names=headers)

print(c1_df.head())

def get_data_from_user(data: pd.DataFrame):
    list_of_init_args = []
    for index in range(len(data.index)):
        ser = c1_df.iloc[index].to_list()
        list_of_init_args.append(ser)
    print(list_of_init_args)

    list_of_pokemon = []
    for a, b, c, d, e, f in list_of_init_args:
        print(type(a), type(b), type(c), type(d), type(e), type(f))
        my_pokemon = Pokemon(a, b, c, d, e, f) #! NO FUNCIONA
        list_of_pokemon.append(my_pokemon)

    return list_of_pokemon

c1 = get_data_from_user(c1_df)
c2 = get_data_from_user(c2_df)

def print_trainer_stats(trainer_list):

    for i in c1:
        print(i)

    for i in c2:
        print(i)

