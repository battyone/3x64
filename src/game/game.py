from __future__ import annotations
from threading import Timer
import game.rules.move
from .models.settings import Settings
from .models.state import State
from .rules.helpers import get_default_pos, is_avaliable, get_random_block
from .rules.tick import tick
from .rules.bonus import use_bonus

class Game:
    def __init__(self, state: State, settings: Settings):
        self.state    : State    = state
        self.settings : Settings = settings
        self.__ticker : Timer    = None

    @staticmethod
    def New_Game(settings: Settings) -> Game:
        return Game(
            state    = State.New_Game(settings),
            settings = settings
        )

    def is_over(self) -> bool:
        return not is_avaliable(self, *get_default_pos(self))

    def start(self):
        self.state.paused = False
        self.state.board.cur_block = get_random_block(self)
        self.state.board.next_block = get_random_block(self)
        self.state.board.cur_pos = get_default_pos(self)
        tick(self)

    def pause(self):
        self.state.paused = not self.state.paused
        if self.state.paused:
            self.__ticker.cancel()
        else:
            tick(self)

    def move_left(self):
        game.rules.move.move_left(self)

    def move_right(self):
        game.rules.move.move_right(self)

    def move_down(self):
        game.rules.move.move_down(self)

    def use_bonus(self, i):
        use_bonus(self, i)
