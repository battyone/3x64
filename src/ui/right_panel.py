def draw_right_panel(ui, screen):
    left_panel_width = 15
    board_width = 2 * ui.get_block_size(screen) * len(ui.game.state.board) + 2
    x = left_panel_width + board_width
    ui.draw_panel(screen, __get(ui), x, 0, ui.colors['ui'])

def __get(ui):
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
