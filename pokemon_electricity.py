from pokemon import Pokemon
from random import randint

class PokemonElectricity(Pokemon):
    def fight_attack(self, pokemon: Pokemon):
        if randint(0, 1) == 1:
            if pokemon.fight_defense(self.get_atq() * 2):
                print("Hit {} for {} points of damage. CRIT DAMAGE".format(pokemon.name, self._atq - pokemon.get_def()))
                return True
            else:
                print("Attack didn't do any damage")
                return False
        else:  # No necesario pero aclara un poco
            return super().fight_attack(pokemon)