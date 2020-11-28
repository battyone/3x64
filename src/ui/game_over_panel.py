def draw_game_over_panel(ui, screen):
    width = ui.get_block_size(screen) * len(ui.game.state.board) * 2
    start_y = width//4 - 1
    ui.draw_panel(screen, __get(ui, width), 15, start_y, ui.colors['ui'])

def __get(ui, width):
    return [
        f"╠{'═' * width}╣",
        f"║{' ' * width}║",
        f"║{' ' * (width//2 - 9)}{'G A M E    O V E R'}{' ' * (width//2 - 9)}║",
        f"║{' ' * width}║",
        f"╠{'═' * width}╣"
    ]
