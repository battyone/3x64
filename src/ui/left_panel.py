def draw_left_panel(ui, screen):
    ui.draw_panel(screen, __get(ui), 0, 0, ui.colors['ui'])

def __get(ui):
    stats = ui.game.stats
    return [
        "┌─Stats────────",
       f"│ Score: {stats.score:05d}",
        "├──────────────",
       f"│ Level: {stats.get_level()}",
        "├──────────────",
       f"│ Time:  {stats.play_time//60:02d}:{stats.play_time%60:02d}",
        "╞═Controls═════",
        "│[a][s][d] Move",
        "│[←][↓][→]",
        "│[P]ause [Q]uit",
        "└──────────────"
    ]
