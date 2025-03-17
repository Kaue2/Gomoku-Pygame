from Peca import Peca
from Player import Player
from PriorityQueue import PriorityQueueGame
from copy import deepcopy
class Game:
    def __init__(self, size_game_board, players=[]):
        self.size = size_game_board
        self.game_board = self.init_game_board(size_game_board)
        self.players = players
        self.current_player = self.players[0]
        self.plays = 0
        self.scale = 25

    def init_game_board(self, size_game_board):
        game_board = []
        line = []
        for _ in range(size_game_board):
            for _ in range(size_game_board):
                line.append('_')
            game_board.append(line)
            line = []
        return game_board

    def play(self, piece:Peca):
        copy_piece = deepcopy(piece)
        line, col = copy_piece.position
        line = int(line/self.scale)
        col = int(col/self.scale)
        copy_piece.position = (line, col)
        if(self.game_board[line][col] == '_'):
            self.game_board[line][col] = copy_piece.player.name
            piece.player.played_pieces.append(copy_piece)
            if(self.verify_win(copy_piece.player)):
                return 'win'
            self.plays += 1
            self.current_player = self.players[self.plays % (len(self.players))]
            return 'ok'
        return 'nok'
    
    def verify_win(self, player:Player):
        if(len(player.played_pieces) >= 5):
            priority_queue = PriorityQueueGame()
            for piece in player.played_pieces:
                priority_queue.enqueue(piece)
            while(not priority_queue.queue.empty()):
                current_piece = priority_queue.dequeue()
                if(
                    self.verify_vertical(current_piece) or
                    self.verify_horizontal(current_piece) or
                    self.verify_first_diagonal(current_piece) or
                    self.verify_second_diagonal(current_piece)
                ): 
                    return True
        return False

    def verify_vertical(self, piece:Peca):
        line, col = piece.position
        initial_line = line
        while(self.game_board[line][col] == piece.player.name): line += 1
        return line - initial_line == 5

    def verify_horizontal(self, piece:Peca):
        line, col = piece.position
        initial_col = col
        while(self.game_board[line][col] == piece.player.name): col += 1
        return col - initial_col == 5

    def verify_first_diagonal(self, piece:Peca):
        line, col = piece.position
        initial_line, initial_col = piece.position
        while(self.game_board[line][col] == piece.player.name and line < self.size and col < self.size):
            line += 1
            col += 1
        print(line, initial_line, col, initial_col)
        return line - initial_line == 5 and col - initial_col == 5
    
    def verify_second_diagonal(self, piece:Peca):
        line, col = piece.position
        initial_line, initial_col = piece.position
        while(self.game_board[line][col] == piece.player.name and col > 0 and line < self.size):
            line += 1
            col -= 1
        return line - initial_line == 5 and initial_col - col == 5
    
    def __repr__(self):
        representation = ''
        for line in self.game_board:
            for col in line:
                representation += f'| {col} |'
            representation += '\n'
        return representation