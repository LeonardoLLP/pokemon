from pokemon import Pokemon
from pokemon_water import PokemonWater
from pokemon_air import PokemonAir
from pokemon_earth import PokemonEarth
from pokemon_electricity import PokemonElectricity

from typing import List, Union
import pandas as pd

filepath_c1 = "coach_1_pokemons.csv"
filepath_c2 = "coach_2_pokemons.csv"


headers = ["ID", "Name", "Move", "hp", "Attack", "Defense"]

c1_df = pd.read_csv(filepath_c1, sep=",", names=headers)
c2_df = pd.read_csv(filepath_c2, sep=",", names=headers)

# print(c1_df.head())

def get_data_from_user(t_name: str, data: pd.DataFrame):
    """Creates trainer with trainer name and data afterwards"""
    list_of_init_args = []

    for index in range(len(data.index)):
        ser = data.iloc[index].to_list()
        list_of_init_args.append(ser)

    list_of_pokemon = []
    for a, b, c, d, e, f in list_of_init_args:
        # print(type(a), type(b), type(c), type(d), type(e), type(f))  # Just to check types
        my_pokemon = Pokemon(a, b, c, d, e, f)
        list_of_pokemon.append(my_pokemon)

    trainer_dict = {
        "name": t_name,
        "pokemons": list_of_pokemon
    }

    return trainer_dict

c1 = get_data_from_user("Ash",   c1_df)
c2 = get_data_from_user("Brook", c2_df)

def print_trainer_stats(trainer: dict):
    """Prints trainer stats"""
    print("{} has:".format(trainer["name"]))
    for pokemon in trainer["pokemons"]:
        print("- {}".format(pokemon))


print_trainer_stats(c1)
print_trainer_stats(c2)


def get_pokemon_in_a_list_of_pokemon(list_of_pokemon: list[Pokemon]):
    """Must be just list with pokemon"""
    while True:
        list_of_names = []
        for pokemon in list_of_pokemon:
            list_of_names.append(pokemon.name)

        # To avoid innecesary errors for capitalization
        list_of_names_casefolded = [name.casefold() for name in list_of_names]

        print("Choose pokemon from {}".format(list_of_names))
        pokemon_str = input().casefold()
        try:
            index = list_of_names_casefolded.index(pokemon_str)
        except:
            print("Pokemon is not in list. Try again.")
            continue

        return list_of_pokemon[index]


def coach_is_undefeated(list_of_pokemon: list[Pokemon]):
    if len(list_of_pokemon) == 0:
        return False
    else:
        return True


# Calls pokemon to fight
def fight(p_attacking: Pokemon, p_defending: Pokemon, l_defending: list[Pokemon]):
    """Fighting between two pokemons

    p_attacking: Pokemon attacking
    p_defending: Pokemon defending
    l_defending: List of trainer defending
    """

    p_attacking.fight_attack(p_defending)

    if p_defending.is_alive() == False:
        print("Pokemon {} was defeated".format(p_defending.name))
        l_defending.remove(p_defending)




def turn(attacking_t, defending_t) -> bool:
    """Normal passing of a turn, returns True if game continues

    attacking_t = Attacking_trainer
    defending_t = Defending_trainer
    """
    print("")




def play_game():
    get_pokemon_in_a_list_of_pokemon(c1["pokemons"])


if __name__ == "__main__":
    play_game()

