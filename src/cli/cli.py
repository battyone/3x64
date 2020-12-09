import curses
from game.game import Game
from .helpers.get_palettes import get_palettes
from .helpers.handle_key import handle_key
from .panels.panels import draw_all

class CLI:
    def __init__(self, game: Game):
        self.game     : Game = game
        self.palettes : {}   = dict()
        curses.wrapper(self.main)

    def main(self, screen):
        curses.curs_set(0)
        screen.keypad(1)
        screen.nodelay(1)
        self.palettes = get_palettes()
        self.game.events.call('client_start')

        while True:
            screen.erase()
            draw_all(self, screen)
            if handle_key(self, screen.getch()) is not None:
                return
