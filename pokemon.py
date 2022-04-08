class Pokemon:
    def __init__(self, id, name, moves, hp, atq, defense):
        """Inicializa un pokemon

        id: int
        name: str
        moves: in "puñetazo", "patada", "codazo", "cabezazo"
        hp: 1 -- 100
        atq: 1 -- 10
        def: 1 -- 10
        """
        c_moves = None
        for move in moves:
            if move in ["puñetazo", "patada", "codazo", "cabezazo"]:
                continue
            c_moves = False
            break
        else:
            c_moves = True

        c_hp = 1 <= hp <= 100
        c_atq = 1 <= atq <= 10
        c_def = 1 <= defense <= 100

        if (c_moves and c_hp and c_atq and c_def):
            self.id = id
            self.name = name
            self._moves = moves
            self._hp = hp
            self._atq = atq
            self._defense = defense
        else:
            raise Exception("Values for pokemon not correct. Check docstring for more info")

    def print_stats(self):
        print("Pokemon ID {} with name {} has as weapon/s") #! not finished


