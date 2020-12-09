from .helpers import get_random_block, get_default_pos

def start(game):
    game.state.started = True
    game.state.paused = False
    game.state.board.next_block = get_random_block()
    game.events.call('started')
