from .helpers import get_all_cols, Sequence
from .gravity import pull_down

def handle_rotation(game):
    def rotate():
        cols : [Sequence] = list(get_all_cols(game.state.board.xy))
        for y in range(len(game.state.board.xy)):
            game.state.board.xy[y] = [block for (block, _, _) in reversed(cols[y])]

    if game.state.time_to_rotate > 0:
        return
    rotate()
    pull_down(game)
    game.state.time_to_rotate = game.settings.max_time_to_rotate

