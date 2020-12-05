from __future__ import annotations

class Block:
    def __init__(self, color: int, danger: bool, iron: bool, name: str, on_place=None):
        self.color    : int  = color
        self.danger   : bool = danger
        self.iron     : bool = iron
        self.name     : str  = name
        if on_place is not None:
            self.on_place = on_place

    def on_place(self, board, x, y):
        board.xy[y][x] = self

    @staticmethod
    def Color(color: int) -> Block:
        return Block(color, False, False, str(color))

    @staticmethod
    def Danger(color: int) -> Block:
        return Block(color, True, False, f'{color}-danger')

    @staticmethod
    def Iron() -> Block:
        return Block(None, False, True, 'iron')

    @staticmethod
    def Bonus(bonus: str, on_place) -> Block:
        return Block(None, False, False, bonus, on_place)
