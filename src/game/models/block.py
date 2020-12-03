from __future__ import annotations

class Block:
    def __init__(self, color: int, danger: bool, iron: bool):
        self.color  : int  = color
        self.danger : bool = danger
        self.iron   : bool = iron

    @staticmethod
    def Color(color: int) -> Block:
        return Block(color, False, False)

    @staticmethod
    def Dange(color: int) -> Block:
        return Block(color, True, False)

    @staticmethod
    def Iron() -> Block:
        return Block(None, False, True)
