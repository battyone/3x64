from game.game import Game
from game.models.settings import Settings
from cli.cli import CLI

game = Game.New_Game(Settings())
client = CLI(game)
