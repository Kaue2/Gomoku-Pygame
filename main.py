from Game import Game
from PyGameConfig import PyGameConfig
from Player import HumanPlayer, IAPlayer

size = 5
scale = 25
points_to_win = 4
players = [
    HumanPlayer('Você','white'),
    IAPlayer('IA', 'red')
]

game = Game(size, players, points_to_win)
pg = PyGameConfig(game, scale)
pg.start_game()