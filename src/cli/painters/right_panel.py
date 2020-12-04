from .painter import draw_panel, get_block_size
from .board import get_board_left, get_board_top

def draw_right_panel(client, screen):
    draw_panel(
        screen,
        __get(client),
        get_board_left(client, screen) + get_block_size(client, screen) * 2 * len(client.game.state.board.xy) + 2,
        get_board_top(client, screen),
        client.palettes['ui'])

def __get(client):
    return [
        "─PowerUps────┬─┐",
        "             │1│",
        "─────────────┼─┤",
        "             │2│",
        "─────────────┼─┤",
        "             │3│",
        "═════════════╪═╡",
        "             │4│",
        "─────────────┼─┤",
        "             │5│",
        "─────────────┴─┘"
    ]
