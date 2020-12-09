from .helpers import get_random_block, get_default_pos

def start_new_block(game):
    if game.state.board.cur_block is not None:
        game.events.unsubscribe('block_fell', game.state.board.cur_block.on_place)
    game.state.board.cur_block = game.state.board.next_block
    game.state.board.next_block = get_random_block()
    game.state.board.cur_pos = get_default_pos(game)
    game.events.subscribe('block_fell', game.state.board.cur_block.on_place)
    game.events.call('block_started', game.state.board.cur_block)
