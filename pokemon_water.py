from pokemon import Pokemon

class PokemonWater(Pokemon):
    def check_atq(self, atq: int):
        if 11 <= atq <= 20:
            return True
        else:
            return False

    # Cambiamos docstring
    def __init__(self, id, name, hp, atq, defense):
        """Inicializa un pokemon

        id: int
        name: str
        move: str in ["puñetazo", "patada", "codazo", "cabezazo"]
        hp:   1 -- 100
        atq: 11 -- 20
        def:  1 -- 10
        """
        super().__init__(id, name, hp, atq, defense)
