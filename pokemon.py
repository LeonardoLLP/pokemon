from enum import Enum
from numpy import int64

class Move(Enum):
    PUÑETAZO = "puñetazo"
    PATADA = "patada"
    CODAZO = "codazo"
    CABEZAZO = "cabezazo"

class Pokemon:
    pass

class Pokemon:
    def check_def(self, defense: int):
        if 1 <= defense <= 10:
            return True
        else:
            return False

    def check_atq(self, atq: int):
        if 1 <= atq <= 10:
            return True
        else:
            return False

    def __init__(self, id: int, name: str, move, hp: int, atq: int, defense: int):
        """Inicializa un pokemon

        id: int
        name: str
        move: Move.str, with str in [PUÑETAZO, PATADA, CODAZO, CABEZAZO]
            OR str in ["]
        hp: 1 -- 100
        atq: 1 -- 10
        def: 1 -- 10
        """

        #* Declaramos método de inicializar con string también
        if type(move) == str:
            if move == "kick":
                move = Move.PATADA
            elif move == "headbutt":
                move = Move.CABEZAZO
            elif move == "elbow":
                move = Move.CODAZO
            elif move == "punch":
                move = Move.PUÑETAZO
            else:
                raise Exception("If move initialized with string, must be valid move (see docstring).")

        c_id = type(id) in [int, int64]
        c_name = type(name) == str
        # c_move = move.value in ["puñetazo", "patada", "codazo", "cabezazo"]
        c_move = move in Move
        c_hp = 1 <= hp <= 100
        c_atq = self.check_atq(atq)
        c_def = self.check_def(defense)

        #_Todos tienen que ser protegidos pero no privados: todos son heredables
        if (c_id and c_name and c_move and c_hp and c_atq and c_def):
            self._enum_move = move
            self.id = id
            self.name = name
            self._move = move.value
            self._hp = hp
            self._atq = atq
            self._defense = defense
        else:
            raise Exception("Values for pokemon not correct. Check docstring for more info")

    def print_stats(self):
        """Prints main stats of pokemon"""
        print("Pokemon ID {} with name {} has as weapon {} and health {}."
              .format(self.id, self.name, self._move.upper(), self._hp))

    #? No necesita getter o setter. Realmente python está programado para que ningún método sea protegido o privado. Aún así, es una buena práctica,
    #? pero este pokemon no cambia nunca su ataque o defense, no evoluciona, y el método de arriba ya hace de getter de los atributos que
    #? se espera obtener del pokemon. Sin embargo, sería conveniente asignar un método que cambiase
    #? los puntos de vida en función del daño que reciba, y además, otra para obtener puntos de defensa y otra para el ataque

    def is_hit(self, hp_to_deduct: int):
        """Deducts hp """
        self._hp -= hp_to_deduct

    def get_def(self):
        return self._defense

    def get_atq(self):
        return self._atq

    def is_alive(self):
        if self._hp < 1:
            print("Pokemon is dead")
            return False
        else:
            print("Pokemon is alive with {}".format(self._hp))
            return True

    def fight_attack(self, pokemon: Pokemon):
        if pokemon.fight_defense(self.get_atq()):
            print("Hit {} for {} points of damage".format(pokemon.name, self._atq - pokemon.get_def()))
            return True
        else:
            print("Attack didn't do any damage")
            return False

    def fight_defense(self, damage: int):
        hp_hit = damage - self.get_def()
        if hp_hit > 0:
            self.is_hit(hp_hit)
            return True
        else:
            return False

    def __str__(self):
        """Print self stats for reference to pokemon"""
        return "Pokemon ID {} with name {} has as weapon {} and health {}.".format(self.id, self.name, self._move.upper(), self._hp)

if __name__ == "__main__":
    p = Pokemon(120, "Bulbasus", Move.CODAZO, 100, 2, 5)
    p.print_stats()

