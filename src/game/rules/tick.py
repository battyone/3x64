from threading import Timer
from .move import move

def tick(game):
    game.state.play_time += 1
    game.state.board.time_to_rotate -= 1

    move(game, 0, 1)
    if not game.is_over():
        set_next_tick(game)

def set_next_tick(game):
    delay = get_tick_delay(game)
    game.ticker = Timer(delay, lambda: tick(game))
    game.ticker.start()

def get_tick_delay(game):
    iron = int(game.state.board.cur_block.iron > 0)
    level = game.state.get_level()
    base_speed = 4/5
    return base_speed - 2/5 * iron - 1/50 * level
