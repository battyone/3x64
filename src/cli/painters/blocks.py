from game.rules.helpers import get_default_pos
from .painter import get_block_size

def draw_blocks(client, screen):
    size = len(client.game.state.board.xy)
    for y in range(size):
        for x in range(size):
            block = client.game.state.board.xy[y][x]
            if block is not None:
                draw_block(client, screen, x, y, block, get_block_symbol(block))

def draw_cur_block(client, screen):
    x, y = client.game.state.board.cur_pos
    block = client.game.state.board.cur_block
    draw_block(client, screen, x, y, block, get_block_symbol(block))

def draw_next_block(client, screen):
    x, y = get_default_pos(client.game)
    block = client.game.state.board.next_block
    draw_block(client, screen, x, y, block, '▓')

def get_block_symbol(block):
    return '▓' if block.iron else '█'

def draw_block(client, screen, x, y, block, char):
    size = get_block_size(client, screen)
    left = 2 * x * size
    top = y * size
    for row in range(size):
        color = 'iron' if block.iron else block.color
        screen.addstr(1 + row + top, 16 + left, char * size * 2, client.palettes[color])