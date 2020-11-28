from threading import Timer
from time import time
from .state import State
from .stats import Stats
from .settings import Settings

class Game:
    def __init__(self, settings: Settings):
        self.settings : Settings = settings
        self.stats    : Stats    = Stats()
        self.state    : State    = State(settings, self.stats)
        self.event = None

    def is_over(self) -> bool:
        return not self.state.is_avaliable(*self.state.get_default_pos())

    def can_move(self) -> bool:
        return not self.is_over() and not self.state.paused

    def start(self):
        self.stats.start_time = time()
        self.state.paused = False
        self.__tick()

    def pause(self):
        self.state.paused = not self.state.paused
        if not self.state.paused:
            self.__tick()
        else:
            self.event.cancel()

    def move_left(self):
        if self.can_move():
            self.state.move_left()

    def move_right(self):
        if self.can_move():
            self.state.move_right()

    def move_down(self):
        if self.can_move():
            self.state.move_down()

    def __tick(self):
        self.stats.play_time+=1
        self.move_down()

        if self.can_move():
            is_stone = self.state.cur_blocks[0] == 0
            delay = 1 / ((1 + is_stone) * self.stats.get_level())
            self.event = Timer(delay, self.__tick)
            self.event.start()
