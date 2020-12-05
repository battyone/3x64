from __future__ import annotations
from .settings import Settings
from .bonus import Bonus
from .board import Board

class State:
    def __init__(self, board: Board, paused: bool, score: int, play_time: int, bonuses: [str]):
        self.board          : Board    = board
        self.paused         : bool     = paused
        self.score          : int      = score
        self.play_time      : int      = play_time
        self.bonuses        : [Bonus]  = bonuses

    def get_level(self) -> int:
        return 1 + self.score // 100

    @staticmethod
    def New_Game(settings: Settings) -> State:
        return State(
            board          = Board.New_Game(settings),
            paused         = True,
            score          = 0,
            play_time      = 0,
            bonuses        = []
        )
