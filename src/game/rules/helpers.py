from typing import Tuple
from random import randint
from ..models.block import Block

def get_default_pos(game) -> (int, int):
    """Return (x,y) for new blocks to start from"""
    return (
        len(game.state.board.xy) // 2,
        0
    )

def is_in_bounds(board, x: int, y: int):
    """Return true if (x,y) is in bounds of the game board"""
    return (0 <= x < len(board.xy) and
            0 <= y < len(board.xy))

def is_avaliable(game, x: int, y: int) -> bool:
    """Return true if (x,y) if in bounds and free of any block"""
    return is_in_bounds(game.state.board, x, y) and game.state.board.xy[y][x] is None

def get_random_block():
    """Return random index of color for a new block"""
    if randint(0, 100) < 10:
        return Block.Iron()
    return Block.Color(randint(0, 3))

Item = Tuple[Block, int, int] # (Block, x, y)
Sequence = [Item]

def get_all_rows(board: [[Block]]) -> [Sequence]:
    """Return all sequences that are board rows"""
    for y in range(len(board)):
        yield [(board[y][x], x, y) for x in range(len(board))]

def get_all_cols(board: [[Block]]) -> [Sequence]:
    """Return all sequences that are board columns"""
    for x in range(len(board)):
        yield [(board[y][x], x, y) for y in range(len(board))]
