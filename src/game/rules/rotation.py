from .helpers import get_all_cols, Sequence
from .gravity import pull_down
from .collision import handle_collisions

def handle_rotation(game):
    def rotate_clockwise():
        cols : [Sequence] = list(get_all_cols(game.state.board.xy))
        for y in range(len(game.state.board.xy)):
            game.state.board.xy[y] = [block for (block, _, _) in reversed(cols[y])]

    def rotate_counterclockwise():
        cols : [Sequence] = list(get_all_cols(game.state.board.xy))
        for y in range(len(cols)):
            game.state.board.xy[-y-1] = [block for (block, _, _) in cols[y]]

    if game.state.time_to_rotate > 0:
        return
    if game.state.board.clockwise:
        rotate_clockwise()
        game.state.board.sides = game.state.board.sides[-1:] + game.state.board.sides[:-1]
    else:
        rotate_counterclockwise()
        game.state.board.sides = game.state.board.sides[1:] + game.state.board.sides[:1]
    pull_down(game)
    handle_collisions(game)
    game.state.time_to_rotate = game.settings.max_time_to_rotate
