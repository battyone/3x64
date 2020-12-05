import curses
from game.game import Game
from .painters.left_panel import draw_left_panel
from .painters.board import draw_board_frame
from .painters.right_panel import draw_right_panel
from .painters.game_over import draw_game_over
from .painters.blocks import draw_blocks, draw_cur_block, draw_next_block
from .painters.pause import draw_pause
from .painters.status_bar import draw_status_bar

class CLI:
    def __init__(self, game: Game):
        self.game     : Game = game
        self.palettes : {}   = dict()
        curses.wrapper(self.main)

    def main(self, screen):
        def init_colors():
            init_color('iron', 8, 0)
            init_color('white', 7, 0)
            init_color('anvil', 234, 234)
            self.palettes['ui'] = self.palettes['iron']
            for i, fg in enumerate([4, 6, 2, 1]):
                init_color(f'{i}-side', 7, fg)
                init_color(f'{i}', fg, 0)

        def init_color(key, fg, bg):
            i = len(self.palettes.keys()) + 1
            curses.init_pair(i, fg, bg)
            self.palettes[key] = curses.color_pair(i)

        def draw_all():
            draw_left_panel(self, screen)
            draw_board_frame(self, screen)
            draw_status_bar(self, screen)
            draw_right_panel(self, screen)
            draw_blocks(self, screen)
            draw_next_block(self, screen)
            draw_cur_block(self, screen)
            if self.game.is_over():
                draw_game_over(self, screen)
            if self.game.state.paused:
                draw_pause(self, screen)

        def handle_key(key):
            if key == ord('q'):
                self.game.pause()
                return False
            if key in [curses.KEY_LEFT, ord('a')]:
                self.game.move_left()
            if key in [curses.KEY_RIGHT, ord('d')]:
                self.game.move_right()
            if key in [curses.KEY_DOWN, ord('s')]:
                self.game.move_down()
            if key == ord('p'):
                self.game.pause()
            if ord('1') <= key <= ord('5'):
                self.game.use_bonus(int(chr(key))-1)

        init_colors()
        curses.curs_set(0)
        screen.keypad(1)
        screen.nodelay(1)
        self.game.start()

        while True:
            screen.erase()
            draw_all()
            if handle_key(screen.getch()) is not None:
                return
