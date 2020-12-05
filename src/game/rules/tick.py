from threading import Timer
from .move import move_down, can_move

def tick(game):
    def set_next_tick():
        delay = get_tick_delay()
        game._Game__ticker = Timer(delay, lambda: tick(game))
        game._Game__ticker.start()

    def get_tick_delay():
        iron = game.state.board.cur_block.iron
        level = game.state.get_level()
        return 1 / (2.5 * level) if iron else 1 / (1.25 * level)

    game.state.play_time += 1
    game.state.board.time_to_rotate -= 1
    move_down(game)

    if can_move(game):
        set_next_tick()
