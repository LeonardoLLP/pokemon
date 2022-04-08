from pokemon import Pokemon
from random import randint

class PokemonAir(Pokemon):
    def fight_defense(self, damage: int):
        if randint(0, 1) == 1:
            return False
        return super().fight_defense(damage)

