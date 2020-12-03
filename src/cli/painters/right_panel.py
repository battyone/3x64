from .painter import draw_panel, get_block_size

def draw_right_panel(client, screen):
    left_panel_width = 15
    board_width = 2 * get_block_size(client, screen) * len(client.game.state.board.xy) + 2
    x = left_panel_width + board_width

    draw_panel(screen, __get(client), x, 0, client.palettes['ui'])

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
