def draw_board_panel(ui, screen):
    ui.draw_panel(screen, __get(ui, screen), 15, 0, ui.colors['ui'])

def __get(ui, screen):
    block = ui.get_block_size(screen)
    count = len(ui.game.state.board)
    return [
            f"╔{'═' * 2 * block * count}╗",
          *[f"║{' ' * 2 * block * count}║" for _ in range(block * count)],
            f"╚{'═' * 2 * block * count}╝"
    ]
