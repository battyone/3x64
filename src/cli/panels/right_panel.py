from ..helpers.painter import draw_panel, get_block_size, draw_data
from .board import get_board_left, get_board_top

def draw_right_panel(client, screen):
    left = get_board_left(client, screen) + get_block_size(client, screen) * 2 * len(client.game.state.board.xy) + 2
    top = get_board_top(client, screen)
    draw_panel(screen, get_frame(), left, top, client.palettes['ui'])

    draw_data(client, screen, left + 1, top, 'PowerUps')
    for i, bonus in enumerate(client.game.state.bonuses):
        draw_data(client, screen, left + 1, top + 1 + (2 * i), f'{bonus.name:12}[{i+1}]')

def get_frame():
    return [
        " PowerUps ───┬─┐",
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
