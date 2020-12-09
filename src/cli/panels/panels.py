from .left_panel import draw_left_panel
from .board import draw_board_frame
from .right_panel import draw_right_panel
from .game_over import draw_game_over
from .blocks import draw_blocks, draw_cur_block, draw_next_block
from .pause import draw_pause
from .status_bar import draw_status_bar

def draw_all(client, screen):
    draw_left_panel(client, screen)
    draw_board_frame(client, screen)
    draw_status_bar(client, screen)
    draw_right_panel(client, screen)
    draw_blocks(client, screen)
    draw_next_block(client, screen)
    draw_cur_block(client, screen)
    if client.game.is_over():
        draw_game_over(client, screen)
    if client.game.state.paused:
        draw_pause(client, screen)
