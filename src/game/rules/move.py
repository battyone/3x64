from .helpers import is_avaliable, get_random_block, get_default_pos
from .collision import handle_collisions
from .rotation import handle_rotation

def can_move(game) -> bool:
    return not (game.is_over() or game.state.paused)

def if_can_move(move):
    return lambda game: move(game) if can_move(game) else None

@if_can_move
def move_left(game):
    x, y = game.state.board.cur_pos
    if is_avaliable(game, x-1, y):
        game.state.board.cur_pos = (x-1, y)

@if_can_move
def move_right(game):
    x, y = game.state.board.cur_pos
    if is_avaliable(game, x+1, y):
        game.state.board.cur_pos = (x+1, y)

@if_can_move
def move_down(game):
    def place_block():
        x, y = game.state.board.cur_pos
        if is_avaliable(game, x, y+1):
            return
        game.state.board.xy[y][x] = game.state.board.cur_block
        start_new_block()
        handle_collisions(game)
        handle_rotation(game)

    def start_new_block():
        game.state.board.cur_block = game.state.board.next_block
        game.state.board.next_block = get_random_block(game)
        game.state.board.cur_pos = get_default_pos(game)

    x, y = game.state.board.cur_pos
    if is_avaliable(game, x, y+1):
        game.state.board.cur_pos = (x, y+1)
    else:
        place_block()
