from __future__ import annotations

class Block:
    def __init__(self, color: int, danger: bool, iron: bool, bonus: str):
        self.color  : int  = color
        self.danger : bool = danger
        self.iron   : bool = iron
        self.bonus  : str  = bonus

    def handle_block_place(self, board, x, y):
        board.xy[y][x] = self

    @staticmethod
    def Color(color: int) -> Block:
        return Block(color, False, False, None)

    @staticmethod
    def Danger(color: int) -> Block:
        return Block(color, True, False, None)

    @staticmethod
    def Iron() -> Block:
        return Block(None, False, True, None)

    @staticmethod
    def Bonus(bonus: str) -> Block:
        return Block(None, False, False, bonus)
