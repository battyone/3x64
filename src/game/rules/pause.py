from .tick import tick

def pause(game, value):
    if game.is_over():
        return
    game.state.paused = value
    if value:
        game.ticker.cancel()
        game.events.call('paused')
    else:
        game.events.call('unpaused')
        tick(game)
