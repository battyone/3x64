from models.settings import Settings
from models.game import Game
from ui.ui import UI

game = Game(Settings())
ui = UI(game)
ui.start()
