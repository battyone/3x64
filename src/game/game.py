from __future__ import annotations
from threading import Timer
from .models.event import Event, EventDispatcher
from .models.settings import Settings
from .models.state import State
from .rules.start import start
from .rules.pause import pause
from .rules.move import move
from .rules.helpers import is_avaliable, get_default_pos
from .rules.start_new_block import start_new_block
from .rules.collisions import check_collisions, delete_blocks, add_points
from .rules.rotation import check_rotation
from .rules.tick import tick
from .rules.gravity import pull_down

class Game:
    def __init__(self, state: State, settings: Settings):
        self.state    : State    = state
        self.settings : Settings = settings
        self.ticker   : Timer    = None
        self.events   = EventDispatcher({
            'started'         : Event(lambda: start_new_block(self),
                                      lambda: tick(self)),
            'paused'          : Event(),
            'unpaused'        : Event(),
            'block_moved'     : Event(),
            'block_fell'      : Event(),
            'block_placed'    : Event(lambda: start_new_block(self),
                                      lambda: check_collisions(self),
                                      lambda: check_rotation(self)),
            'block_started'   : Event(),
            'found_collisions': Event(lambda blocks: delete_blocks(self, blocks),
                                      lambda blocks: add_points(self, blocks),
                                      lambda _: pull_down(self),
                                      lambda _: check_collisions(self)),
            'board_rotated'   : Event(lambda _: pull_down(self),
                                      lambda _: check_collisions(self)),
            'pulled_down'     : Event(),

            'client_down'     : Event(lambda: move(self, 0, 1)),
            'client_left'     : Event(lambda: move(self, -1, 0)),
            'client_right'    : Event(lambda: move(self, 1, 0)),
            'client_pause'    : Event(lambda: pause(self, not self.state.paused)),
            'client_start'    : Event(lambda: start(self))
        })
        self.is_over = lambda: not is_avaliable(self, *get_default_pos(self))

    @staticmethod
    def New_Game(settings: Settings) -> Game:
        return Game(
            state    = State.New_Game(settings),
            settings = settings
        )
