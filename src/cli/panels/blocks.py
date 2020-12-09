from game.rules.helpers import get_default_pos
from ..helpers.painter import get_block_size
from .board import get_board_left, get_board_top

def draw_blocks(client, screen):
    size = len(client.game.state.board.xy)
    for y in range(size):
        for x in range(size):
            block = client.game.state.board.xy[y][x]
            if block is not None:
                draw_block(client, screen, x, y, block)

def draw_cur_block(client, screen):
    x, y = client.game.state.board.cur_pos
    block = client.game.state.board.cur_block
    draw_block(client, screen, x, y, block)

def draw_next_block(client, screen):
    x, y = get_default_pos(client.game)
    block = client.game.state.board.next_block
    draw_block(client, screen, x, y, block)

def get_block_symbol(client, block):
    if block.iron == 2:
        return '╳'
    if block.iron == 1:
        return 'x'
    if block.color == client.game.state.board.sides[0]:
        return '?'
    if block.name == 'anvil':
        return '╪'
    return '█'

def get_block_palette(client, block):
    if block.color == client.game.state.board.sides[0]:
        return client.palettes[f'{block.color}-side']
    return client.palettes[block.name]

def draw_block(client, screen, x, y, block):
    size = get_block_size(client, screen)
    left = 2 * x * size + get_board_left(client, screen)
    top = y * size + get_board_top(client, screen)
    for row in range(size):
        palette = get_block_palette(client, block)
        screen.addstr(1 + row + top, 1 + left, get_block_symbol(client, block) * size * 2, palette)
