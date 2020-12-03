def draw_panel(screen, panel: [str], start_x, start_y, palette):
    for i, line in enumerate(panel):
        screen.addstr(start_y + i, start_x, line, palette)

def get_block_size(client, screen):
    y, x = screen.getmaxyx()
    return min(
        (y-3) // len(client.game.state.board.xy),
        (x-16-17) // (2 * len(client.game.state.board.xy))
    )
