from __future__ import annotations

class Block:
    def __init__(self, color: int, danger: bool, iron: bool, name: str, on_place):
        self.color    : int  = color
        self.danger   : bool = danger
        self.iron     : int  = iron
        self.name     : str  = name
        self.on_place = on_place

    @staticmethod
    def Color(color: int) -> Block:
        return Block(color, False, False, str(color), default_on_place)

    @staticmethod
    def Danger(color: int) -> Block:
        return Block(color, True, False, f'{color}-danger', default_on_place)

    @staticmethod
    def Iron() -> Block:
        return Block(None, False, True, 'iron', default_on_place)

    @staticmethod
    def Bonus(bonus: str) -> Block:
        return Block(None, False, False, bonus, default_on_place)

def default_on_place(game):
    x, y = game.state.board.cur_pos
    game.state.board.xy[y][x] = game.state.board.cur_block
