from .painter import get_block_size, draw_panel

def draw_game_over(client, screen):
    width = get_block_size(client, screen) * len(client.game.state.board.xy) * 2
    start_y = width//4 - 1
    draw_panel(screen, __get(client, width), 15, start_y, client.palettes['ui'])

def __get(client, width):
    return [
        f"╠{'═' * width}╣",
        f"║{' ' * width}║",
        f"║{' ' * (width//2 - 9)}{'G A M E    O V E R'}{' ' * (width//2 - 9)}║",
        f"║{' ' * width}║",
        f"╠{'═' * width}╣"
    ]
