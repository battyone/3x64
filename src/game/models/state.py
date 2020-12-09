from __future__ import annotations
from .settings import Settings
from .bonus import Bonus
from .board import Board

class State:
    def __init__(self, board: Board, started: bool, paused: bool, score: int, play_time: int, bonuses: [str], score_to_level: int):
        self.board          : Board     = board
        self.started        : bool      = started
        self.paused         : bool      = paused
        self.score          : int       = score
        self.play_time      : int       = play_time
        self.bonuses        : [Bonus]   = bonuses
        self.score_to_level : int       = score_to_level

    def get_level(self) -> int:
        return 1 + self.score // self.score_to_level

    @staticmethod
    def New_Game(settings: Settings) -> State:
        return State(
            board          = Board.New_Game(settings),
            started        = False,
            paused         = True,
            score          = 0,
            play_time      = 0,
            bonuses        = [],
            score_to_level = settings.score_to_level
        )
