import curses

def get_palettes():
    palettes = dict()

    def init_color(key, fg, bg):
        i = len(palettes.keys()) + 1
        curses.init_pair(i, fg, bg)
        palettes[key] = curses.color_pair(i)

    init_color('iron', 0, 8)
    init_color('white', 7, 0)
    init_color('anvil', 8, 234)
    init_color('ui', 8, 0)

    for i, fg in enumerate([4, 6, 2, 1]):
        init_color(f'{i}-side', 7, fg)
        init_color(f'{i}', fg, 0)

    return palettes
