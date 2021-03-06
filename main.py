from pokemon import Pokemon
from pokemon_water import PokemonWater
from pokemon_air import PokemonAir
from pokemon_earth import PokemonEarth
from pokemon_electricity import PokemonElectricity

from typing import List, Union
import pandas as pd
from time import sleep

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

trainer1 = get_data_from_user("Ash",   c1_df)
trainer2 = get_data_from_user("Brook", c2_df)

trainer_type = dict[str, Union[str, list[Pokemon]]]

def print_trainer_stats(trainer: dict[str, Union[str, list[Pokemon]]]):
    """Prints trainer stats"""
    print("{} has:".format(trainer["name"]))
    for pokemon in trainer["pokemons"]:
        print("- {}".format(pokemon))


# print_trainer_stats(trainer1)
# print_trainer_stats(trainer2)


def names_of_pokemon(list_of_pokemon: list[Pokemon]):
    list_of_names = []
    for pokemon in list_of_pokemon:
        list_of_names.append(pokemon.name)
    return list_of_names

def name_list_to_str(my_list: list):
    final_str = ""
    for string in my_list:
        final_str += string + ", "
    final_str = final_str.removesuffix(", ")
    return final_str



def get_pokemon_in_a_list_of_pokemon(list_of_pokemon: list[Pokemon]):
    """Expects just list with pokemon,
    ALWAAYS returns a pokemon
    """
    while True:
        list_of_names = names_of_pokemon(list_of_pokemon)

        # To avoid innecesary errors for capitalization
        list_of_names_casefolded = [name.casefold() for name in list_of_names]

        pokemon_str = input().casefold()
        try:
            index = list_of_names_casefolded.index(pokemon_str)
        except:
            print("Pokemon is not in list. List = {}".format(list_of_pokemon))
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

    print("{} is attacking {}".format(attacking_t["name"], defending_t["name"]))
    sleep(2)
    print("{}, choose your attacking pokmeon".format(attacking_t["name"]))
    sleep(0.5)
    print("from {}:".format(
        name_list_to_str(names_of_pokemon(attacking_t["pokemons"]))
        ))
    attacking_p = get_pokemon_in_a_list_of_pokemon(attacking_t["pokemons"])

    sleep(0.5)
    print("Now choose pokemon to attack")
    sleep(0.5)
    print("from {}:".format(
        name_list_to_str(names_of_pokemon(defending_t["pokemons"]))
        ))
    defending_p = get_pokemon_in_a_list_of_pokemon(defending_t["pokemons"])

    sleep(0.5)
    print("{} attacks {}".format(attacking_p.name, defending_p.name))

    fight(attacking_p, defending_p, defending_t["pokemons"])

    sleep(1)

    return coach_is_undefeated(defending_t["pokemons"])




#! Now used to debuge
def play_game(player1_data: tuple[str, pd.DataFrame], player2_data: tuple[str ,pd.DataFrame]):
    trainer1 = get_data_from_user(*player1_data)
    trainer2 = get_data_from_user(*player2_data)

    print("In this legendary match the unbeatable {} will fight the unstopable {}".format(trainer1["name"], trainer2["name"]))
    sleep(2)
    print("=== BEGIN THE FIGHT ===")
    sleep(2)

    trainer1_alive = trainer2_alive = True
    while trainer1_alive and trainer2_alive:
        print_trainer_stats(trainer1)
        print_trainer_stats(trainer2)

        # Create copy to conserve if pokemon dies mid-turn, according to specifications for exercise
        trainer2_copy = {
            "name": trainer2["name"],
            "pokemons": trainer2["pokemons"].copy(),
        }

        trainer2_alive = turn(trainer1, trainer2)
        trainer1_alive = turn(trainer2_copy, trainer1)

    # Logic for both dead
    if not (trainer1_alive or trainer2_alive):
        print("Both trainers are dead. It's a draw!")
    elif not trainer1_alive:
        print("{} was defeated. {} wins the match!".format(trainer1["name"], trainer2["name"]))
    else:  # not trainer2_alive:
        print("{} was defeated. {} wins the match!".format(trainer2["name"], trainer1["name"]))

    sleep(1)

    print("=== GAME ENDED ===")



if __name__ == "__main__":
    print("--- LOADING GAME ---")
    sleep(1)
    name1 = input("Name the first trainer: ")
    name2 = input("Name the second trainer: ")
    play_game((name1, c1_df), (name2, c2_df))

