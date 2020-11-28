import curses
from models.game import Game
from .left_panel import draw_left_panel
from .right_panel import draw_right_panel
from .board_panel import draw_board_panel
from .game_over_panel import draw_game_over_panel

class UI:
    def __init__(self, game: Game):
        self.game       : Game = game
        self.last_score : int  = 0
        self.colors     : {}   = dict()

    def start(self):
        curses.wrapper(self.main)

    def main(self, screen):
        self.init_colors()
        curses.curs_set(0)
        screen.keypad(1)
        screen.nodelay(1)
        self.game.start()

        while True:
            screen.erase()
            self.draw(screen)
            if not self.handle_key(screen.getch()):
                return

    def init_colors(self):
        self.init_color('ui', 8, 0)
        for i, color in enumerate([8, 4, 6, 2, 1]):
            self.init_color(str(i), color, 0)

    def init_color(self, key, fg, bg):
        i = len(self.colors.keys()) + 1
        curses.init_pair(i, fg, bg)
        self.colors[key] = curses.color_pair(i)

    def draw(self, screen):
        state = self.game.state
        draw_left_panel(self, screen)
        draw_right_panel(self, screen)
        draw_board_panel(self, screen)
        self.draw_blocks(screen)
        self.draw_block(screen, *state.get_default_pos(), state.cur_blocks[1], '▓')
        self.draw_block(screen, *state.cur_pos,state.cur_blocks[0], UI.get_block_symbol(self.game.state.cur_blocks[0]))
        if self.game.stats.score != self.last_score:
            self.last_score = self.game.stats.score
            curses.beep()
        if self.game.is_over():
            draw_game_over_panel(self, screen)

    def handle_key(self, key):
        if key == ord('q'):
            self.game.pause()
            return False
        if key == curses.KEY_LEFT or key == ord('a'):
            self.game.move_left()
        if key == curses.KEY_RIGHT or key == ord('d'):
            self.game.move_right()
        if key == curses.KEY_DOWN or key == ord('s'):
            self.game.move_down()
        if key == ord('p'):
            self.game.pause()

        return True

    @staticmethod
    def draw_panel(screen, array, start_x, start_y, color):
        for i, line in enumerate(array):
            screen.addstr(start_y + i, start_x, line, color)

    def get_block_size(self, screen):
        y, x = screen.getmaxyx()
        return min(
            (y-3) // len(self.game.state.board),
            (x-16-17) // (2*len(self.game.state.board))
        )

    def draw_blocks(self, screen):
        size = len(self.game.state.board)
        for y in range(size):
            for x in range(size):
                block = self.game.state.board[y][x]
                if block != ' ':
                    self.draw_block(screen, x, y, block, UI.get_block_symbol(block))

    @staticmethod 
    def get_block_symbol(block):
        return '▓' if block == ' ' else '█'

    def draw_block(self, screen, x, y, block, char):
        size = self.get_block_size(screen)
        left = 2 * x * size
        top = y * size
        for row in range(size):
            screen.addstr(1 + row + top, 16 + left, char * size * 2, self.colors[block])
