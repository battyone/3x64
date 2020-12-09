from ..helpers.painter import get_block_size, draw_panel
from .board import get_board_top, get_board_left

def draw_game_over(client, screen):
    width = get_block_size(client, screen) * len(client.game.state.board.xy) * 2
    draw_panel(
        screen,
        __get(client, width),
        get_board_left(client, screen),
        get_board_top(client, screen) + width//4 - 1,
        client.palettes['ui']
    )

def __get(client, width):
    return [
        f"╠{'═' * width}╣",
        f"║{' ' * width}║",
        f"║{' ' * (width//2 - 9)}{'G A M E    O V E R'}{' ' * (width//2 - 9)}║",
        f"║{' ' * width}║",
        f"╠{'═' * width}╣"
    ]
