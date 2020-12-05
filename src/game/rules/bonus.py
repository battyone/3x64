from random import choice
from ..models.block import Block
from .helpers import is_in_bounds

bonuses = ['Anvil']

def give_random_bonus(game):
    game.state.bonuses.append(
        choice(bonuses)
    )

def use_bonus(game, i):
    if len(game.state.bonuses) < i:
        return
    bonus = game.state.bonuses.pop(i)

    if bonus == 'Anvil':
        game.state.board.next_block = Block.Bonus(bonus)
        game.state.board.next_block.handle_block_place = place_anvil

def place_anvil(board, x, y):
    for dy in range(1, 4):
        if is_in_bounds(board, x, y + dy):
            board.xy[y + dy][x] = None
