from __future__ import annotations
from .settings import Settings
from .board import Board

class State:
    def __init__(self, board: Board, paused: bool, score: int, play_time: int,
                 time_to_rotate: int, bonuses: [str]):
        self.board          : Board    = board
        self.paused         : bool     = paused
        self.score          : int      = score
        self.play_time      : int      = play_time
        self.time_to_rotate : int      = time_to_rotate
        self.bonuses        : [str]    = bonuses

    @staticmethod
    def New_Game(settings: Settings) -> State:
        return State(
            board          = Board.New_Game(settings),
            paused         = True,
            score          = 0,
            play_time      = 0,
            time_to_rotate = settings.max_time_to_rotate,
            bonuses        = []
        )

    def get_level(self) -> int:
        return 1 + self.score // 100
