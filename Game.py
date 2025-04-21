from copy import deepcopy
from Player import Player
from PriorityQueue import PriorityQueueGame
class Game:
    def __init__(self, size_game_board, players=[], points_to_win=5):
        self.size = size_game_board
        self.game_board = self.init_game_board(size_game_board)
        self.players:list[Player] = players
        self.current_player: Player = self.players[0]
        self.plays = 0
        self.scale = 25
        self.points_to_win = points_to_win

    def init_game_board(self, size_game_board):
        game_board = []
        line = []
        for _ in range(size_game_board):
            for _ in range(size_game_board):
                line.append('_')
            game_board.append(line)
            line = []
        return game_board

    def create_valid_plays(self)->list:
        response = []
        for iline, line in enumerate(self.game_board):
            for icol,col in enumerate(line):
                if(col == '_'): response.append((iline, icol))
        return response

    def play(self, piece):
        copy_piece = deepcopy(piece)
        line, col = copy_piece.position
        line = int(line/self.scale)
        col = int(col/self.scale)
        copy_piece.position = (line, col)
        if(self.game_board[line][col] == '_'):
            self.game_board[line][col] = copy_piece.player.name
            piece.player.played_pieces.append(copy_piece)    
            player_points = self.verify_win(copy_piece.player) 
            if(player_points >= self.points_to_win):
                for i, _ in enumerate(self.players):
                    if(i != self.plays % (len(self.players))):
                        self.players[i].status = 'loose'
                self.current_player.status = 'win'

            if(len(self.create_valid_plays()) == 0):
                for i, _ in enumerate(self.players):
                    if(i != self.plays % (len(self.players))):
                        self.players[i].status = 'tied'
                self.current_player.status = 'tied'

            self.plays += 1
            self.current_player.points = player_points
            self.current_player = self.players[self.plays % (len(self.players))]
        return 'nok'
    
    def verify_win(self, player):
        priority_queue = PriorityQueueGame()
        for piece in player.played_pieces:
            priority_queue.enqueue(piece)
        while(not priority_queue.queue.empty()):
            current_piece = priority_queue.dequeue()
            return max(
                self.verify_vertical(current_piece),
                self.verify_horizontal(current_piece),
                self.verify_first_diagonal(current_piece)[0],
                self.verify_second_diagonal(current_piece)[0]
            )
        return 0
    def verify_vertical(self, piece):
        line, col = piece.position
        initial_line = line
        while(line < self.size and self.game_board[line][col] == piece.player.name): line += 1
        return line - initial_line

    def verify_horizontal(self, piece):
        line, col = piece.position
        initial_col = col
        while(col < self.size and self.game_board[line][col] == piece.player.name): col += 1
        return col - initial_col

    def verify_first_diagonal(self, piece):
        line, col = piece.position
        initial_line, initial_col = piece.position

        while(line < self.size and col < self.size and self.game_board[line][col] == piece.player.name):
            line += 1
            col += 1
        return (line - initial_line, col - initial_col) 
    
    def verify_second_diagonal(self, piece):
        line, col = piece.position
        initial_line, initial_col = piece.position
        while(line < self.size and col < self.size and self.game_board[line][col] == piece.player.name):
            line += 1
            col -= 1
        return (line - initial_line, initial_col - col)
    
    def __repr__(self):
        representation = ''
        for line in self.game_board:
            for col in line:
                representation += f'| {col} |'
            representation += '\n'
        return representation