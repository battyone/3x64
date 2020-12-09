from .helpers import is_avaliable

ALLOWED_MOVES = [(1, 0), (-1, 0), (0, 1)]

def can_move(game) -> bool:
    return not (game.is_over() or game.state.paused)

def move(game, dx, dy):
    if (not can_move(game) or (dx, dy) not in ALLOWED_MOVES):
        return
    new_pos = get_new_pos(game, dx, dy)

    if is_avaliable(game, *new_pos):
        game.state.board.cur_pos = new_pos
        game.events.call('block_moved')
    else:
        if (dx, dy) == (0, 1):
            game.events.call('block_fell', game)
            game.events.call('block_placed')

def get_new_pos(game, dx, dy):
    x, y = game.state.board.cur_pos
    return x + dx, y + dy
