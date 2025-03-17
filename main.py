from PyGameConfig import PyGameConfig
from Game import Game
from Player import Player

size = 15
scale = 25

players = [
    Player('j1','white'),
    Player('j2', 'red')
]

game = Game(size, players)
pg = PyGameConfig(game, scale)
pg.start_game()