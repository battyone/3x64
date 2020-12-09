from ..helpers.painter import draw_panel, draw_data
from .board import get_board_left, get_board_top

def draw_left_panel(client, screen):

    left = get_board_left(client, screen) - 15
    top = get_board_top(client, screen)
    state = client.game.state

    draw_panel(screen, get_frame(), left, top, client.palettes['ui'])
    draw_data(client, screen, left+2, top, 'Stats')
    draw_data(client, screen, left+9, top+1, f'{state.score:05d}')
    draw_data(client, screen, left+9, top+3, f'{state.get_level()}')
    draw_data(client, screen, left+9, top+5, f'{state.play_time//60:02d}:{state.play_time%60:02d}')
    draw_data(client, screen, left+2, top+6, 'Controls')

def get_frame():
    return [
        "┌ Stats ───────",
        "│ Score: ",
        "├──────────────",
        "│ Level: ",
        "├──────────────",
        "│ Time:  ",
        "╞ Controls ════",
        "│ [1]—[5] Bonus",
        "│[a][s][d] Move",
        "│[P]ause [Q]uit",
        "└──────────────"
    ]
