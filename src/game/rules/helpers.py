from random import randint
from ..models.block import Block

def get_default_pos(game) -> (int, int):
    return (
        len(game.state.board.xy) // 2,
        0
    )

def is_avaliable(game, x: int, y: int) -> bool:
    return (0 <= x < len(game.state.board.xy) and
            0 <= y < len(game.state.board.xy) and
            game.state.board.xy[y][x] is None
    )

def get_random_block(game):
    if randint(0, 100) < 20:
        return Block.Iron()
    return Block.Color(randint(0, 3))

Item = tuple[Block, int, int] # (Block, x, y)
Sequence = [Item]

def get_all_rows(board: [[Block]], predicate=lambda _: True) -> [Sequence]:
    for y in range(len(board)):
        yield [(board[y][x], x, y) for x in range(len(board)) if predicate(board[y][x])]

def get_all_cols(board: [[Block]], predicate=lambda _: True) -> [Sequence]:
    for x in range(len(board)):
        yield [(board[y][x], x, y) for y in range(len(board)) if predicate(board[y][x])]
