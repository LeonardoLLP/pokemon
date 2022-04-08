class Pokemon:
    def __init__(self, id, name, move, hp, atq, defense):
        """Inicializa un pokemon

        id: int
        name: str
        moves: in "puñetazo", "patada", "codazo", "cabezazo"
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
        print("Pokemon ID {} with name {} has as weapon {} and health {}."
              .format(self.id, self.name))


