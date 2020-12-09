from .helpers import get_all_cols, Sequence

def check_rotation(game):
    board = game.state.board
    if board.time_to_rotate > 0:
        return

    board.time_to_rotate = game.settings.max_time_to_rotate
    cols : [Sequence] = list(get_all_cols(board.xy))

    if board.clockwise:
        rotate_clockwise(board, cols)
        game.events.call('board_rotated', True)
    else:
        rotate_counterclockwise(board, cols)
        game.events.call('board_rotated', False)

def rotate_clockwise(board, cols):
    board.sides = board.sides[-1:] + board.sides[:-1]
    for y in range(len(cols)):
        board.xy[y] = [block for (block, _, _) in reversed(cols[y])]

def rotate_counterclockwise(board, cols):
    board.sides = board.sides[1:] + board.sides[:1]
    for y in range(len(cols)):
        board.xy[-(y+1)] = [block for (block, _, _) in cols[y]]
