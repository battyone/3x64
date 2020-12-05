from ..models.block import Block
from .helpers import Sequence, Item, get_all_rows, get_all_cols
from .gravity import pull_down
from .bonuses import give_random_bonus

def handle_collisions(game):
    def get_blocks_to_delete():
        for sequence in get_all_sequences(game.state.board.xy):
            yield from get_blocks_to_delete_from_sequence(sequence)

    def get_blocks_to_delete_from_sequence(sequence: Sequence) -> [Item]:
        chain : [Item] = []
        for (block, x, y) in sequence:
            last = chain[-1][0] if chain else None
            if can_combine(last, block):
                chain.append((block, x, y))
            else:
                if is_good_chain(chain):
                    yield from chain
                chain = [(block, x, y)]
        if is_good_chain(chain):
            yield from chain

    def can_combine(first: Block, second: Block) -> bool:
        return (
            first is not None and
            second is not None and
            first.color == second.color and
            not (first.iron or second.iron)
        )

    def is_good_chain(chain: [Item]) -> bool:
        return len(chain) >= 3

    def get_all_sequences(board: [[Block]]) -> [Sequence]:
        yield from get_all_rows(board)
        yield from get_all_cols(board)

    blocks : [Item] = list(get_blocks_to_delete())
    if blocks:
        game.state.last_event = (game.state.play_time, f'+{len(blocks)}')
        for (_, x, y) in blocks:
            game.state.board.xy[y][x] = None
        pull_down(game)
        handle_collisions(game)
    if game.state.board.sides[0] in list(map(lambda item: item[0].color, blocks)):
        game.state.score += 2 * len(blocks)
        give_random_bonus(game)
    else:
        game.state.score += len(blocks)
