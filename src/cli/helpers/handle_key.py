import curses

def handle_key(client, key: int):
    """Return false to exit the client"""
    if key == ord('q'):
        client.game.events.call('client_pause')
        return False
    if key in [curses.KEY_LEFT, ord('a')]:
        client.game.events.call('client_left')
    if key in [curses.KEY_RIGHT, ord('d')]:
        client.game.events.call('client_right')
    if key in [curses.KEY_DOWN, ord('s')]:
        client.game.events.call('client_down')
    if key == ord('p'):
        client.game.events.call('client_pause')
    # if ord('1') <= key <= ord('5'):
    #     client.game.use_bonus(int(chr(key))-1)
