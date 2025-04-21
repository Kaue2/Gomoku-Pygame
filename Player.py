from abc import ABC
from Peca import Peca
from copy import deepcopy

class Player(ABC):
    def __init__(self,name, color, min_max=False):
        self.name = name
        self.played_pieces = []
        self.color = color
        # False = min, True = max
        self.min_max = min_max
        self.status = 'playing'
        self.points = 0

    def create_piece_play(self, line, col):
        return Peca(line, col, self)
    
    def __repr__(self):
        return f'({self.name}, {self.color}, {len(self.played_pieces)})'

class HumanPlayer(Player):
    def __init__(self, name, color):
        super().__init__(name, color, False)
        
class IAPlayer(Player):
    def __init__(self, name, color):
        super().__init__(name, color, True)
        self.max_plays_simulated = 1

    def minimax_alfabetaprunnig(self, game, current_player, max_deep, alfa = float('-inf'), beta=float('inf')):
        if(max_deep == 0):
            return  -current_player.points if(current_player.min_max) else current_player.points 
        
        if(current_player.min_max):
            for play in game.create_valid_plays():
                game_copy = deepcopy(game)
                jogada = game_copy.current_player.create_piece_play(play[0]*game.scale,play[1]*game.scale)
                game_copy.play(jogada)
                utility = self.minimax_alfabetaprunnig(game_copy, game_copy.current_player, max_deep-1, alfa, beta)
                alfa = max(utility, alfa)
                if (alfa > beta): break
            return alfa
        else:
            for play in game.create_valid_plays():
                game_copy = deepcopy(game)
                jogada = game_copy.current_player.create_piece_play(play[0]*game_copy.scale,play[1]*game_copy.scale)
                game_copy.play(jogada)
                utility = self.minimax_alfabetaprunnig(game_copy, game_copy.current_player, max_deep-1, alfa, beta)
                beta = min(utility, beta)
                if (alfa > beta): break
            return beta

    def define_an_play(self, game):
        melhor_valor = float('-inf')
        melhor_jogada = None
        copy_game = deepcopy(game)
        for play in copy_game.create_valid_plays():
            jogada = game.current_player.create_piece_play(play[0]*game.scale, play[1]*game.scale)
            copy_game.play(jogada)
            utility = self.minimax_alfabetaprunnig(copy_game, game.current_player,self.max_plays_simulated)
            if(utility > melhor_valor):
                melhor_valor = utility
                melhor_jogada = jogada
        return melhor_jogada