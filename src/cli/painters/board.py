from .painter import get_block_size, draw_panel

def draw_board_frame(client, screen):
    draw_panel(
        screen,
        get_board(client, screen),
        get_board_left(client, screen),
        get_board_top(client, screen),
        client.palettes['ui']
    )

def get_board(client, screen):
    block = get_block_size(client, screen)
    count = len(client.game.state.board.xy)
    width = 2 * block * count
    progress = __get_progress(client, width)
    return [
            f"╔{'═' * width}╗",
          *[f"║{' ' * width}║" for _ in range(block * count)],
            f"╚{'═' * progress + '┄' * (width - progress)}╝"
    ]

def __get_progress(client, width):
    return max(0, client.game.state.time_to_rotate) * width // client.game.settings.max_time_to_rotate

def get_board_left(client, screen):
    y, x = screen.getmaxyx()
    block = get_block_size(client, screen)
    count = len(client.game.state.board.xy)
    return x // 2 - block * count - 1

def get_board_top(client, screen):
    y, x = screen.getmaxyx()
    block = get_block_size(client, screen)
    count = len(client.game.state.board.xy)
    return y // 2 - block * count // 2 - 1
