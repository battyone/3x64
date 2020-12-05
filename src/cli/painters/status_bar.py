from .painter import draw_data
from .board import get_board_left, get_board_top, get_block_size

def draw_status_bar(client, screen):
    if client.game.state.last_event is None:
        return
    time, message = client.game.state.last_event

    if time + 1 < client.game.state.play_time:
        return
    board_width = 2 * get_block_size(client, screen) * len(client.game.state.board.xy)
    left = get_board_left(client, screen) + board_width // 2 - len(message) // 2

    draw_data(client, screen, left, get_board_top(client, screen), f' {message} ')
