from .helpers import get_all_cols, Sequence

def pull_down(game):
    def set_col(x: int, col: Sequence):
        for y, block in enumerate(get_padded_col(col)):
            game.state.board.xy[y][x] = block

    def get_padded_col(col: Sequence) -> Sequence:
        return [None for x in range(size-len(col))] + [block for (block, x, y) in col]

    size = len(game.state.board.xy)
    cols = get_all_cols(game.state.board.xy, lambda block: block is not None)
    for i, col in enumerate(cols):
        set_col(i, col)
