class Pokemon:
    pass

class Pokemon:
    def __init__(self, id: int, name: str, move: str, hp: int, atq: int, defense: int):
        """Inicializa un pokemon

        id: int
        name: str
        move: str in ["puñetazo", "patada", "codazo", "cabezazo"]
        hp: 1 -- 100
        atq: 1 -- 10
        def: 1 -- 10
        """

        c_id = type(id) == int
        c_name = type(name) == str
        c_move = move in ["puñetazo", "patada", "codazo", "cabezazo"]
        c_hp = 1 <= hp <= 100
        c_atq = 1 <= atq <= 10
        c_def = 1 <= defense <= 100

        # Todos tienen que ser protegidos pero no privados: todos son heredables
        if (c_id and c_name and c_move and c_hp and c_atq and c_def):
            self.id = id
            self.name = name
            self._move = move
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
    #? los puntos de vida en función del daño que reciba, y además, otra para obtener puntos de defensa

    def is_hit(self, hp_to_deduct: int):
        """Deducts hp """
        self._hp -= hp_to_deduct

    def is_alive(self):
        if self._hp < 1:
            print("Pokemon is dead")
            return False
        else:
            print("Pokemon is alive with {}".format(self._hp))
            return True

    def fight_attack(self, pokemon: Pokemon):
        if pokemon.fight_defense(self._atq):
            print("Hit {} for {} points of damage".format(pokemon.name, self._atq - pokemon._defense))
            return True
        else:
            print("Attack didn't do any damage")
            return False







