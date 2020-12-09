def pull_down(game):
    board = game.state.board.xy
    for i in range(len(board)):
        pull_down_col(board, i)
    game.events.call('pulled_down')

def pull_down_col(board, x: int):
    blocks = [board[y][x] for y in range(len(board)) if board[y][x] is not None]
    nones = [None for _ in range(len(board) - len(blocks))]

    for y, block in enumerate(nones + blocks):
        board[y][x] = block
