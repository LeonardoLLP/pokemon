from pokemon import Pokemon

class PokemonEarth(Pokemon):
    def check_def(self, defense: int):
        if 11 <= defense <= 20:
            return True
        else:
            return False

    # Cambiamos docstring
    def __init__(self, id, name, hp, atq, defense):
        """Inicializa un pokemon

        id: int
        name: str
        move: Move.str, with str in [PUÑETAZO, PATADA, CODAZO, CABEZAZO]
        hp: 1 -- 100
        atq: 1 -- 10
        def: 11 -- 20
        """
        super().__init__(id, name, hp, atq, defense)

