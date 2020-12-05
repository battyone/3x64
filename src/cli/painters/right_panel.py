from .painter import draw_panel, get_block_size
from .board import get_board_left, get_board_top

def draw_right_panel(client, screen):
    left = get_board_left(client, screen) + get_block_size(client, screen) * 2 * len(client.game.state.board.xy) + 2
    top = get_board_top(client, screen)
    draw_panel(screen, get_frame(), left, top, client.palettes['ui'])
    for i, label in enumerate(client.game.state.bonuses):
        draw_panel(screen, [label[:12].ljust(12)+f'[{i+1}]'], left+1, top+1+2*i, client.palettes['white'])

def get_frame():
    return [
        "─PowerUps────┬─┐",
        "             │ │",
        "─────────────┼─┤",
        "             │ │",
        "─────────────┼─┤",
        "             │ │",
        "═════════════╪═╡",
        "             │ │",
        "─────────────┼─┤",
        "             │ │",
        "─────────────┴─┘"
    ]
