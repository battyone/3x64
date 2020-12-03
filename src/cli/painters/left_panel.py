from .painter import draw_panel

def draw_left_panel(client, screen):
    draw_panel(screen, __get(client), 0, 0, client.palettes['ui'])

def __get(client):
    state = client.game.state
    return [
        "┌─Stats────────",
       f"│ Score: {state.score:05d}",
        "├──────────────",
       f"│ Level: {state.get_level()}",
        "├──────────────",
       f"│ Time:  {state.play_time//60:02d}:{state.play_time%60:02d}",
        "╞═Controls═════",
        "│[a][s][d] Move",
        "│[←][↓][→]",
        "│[P]ause [Q]uit",
        "└──────────────"
    ]
