class Peca:
    def __init__(self, pos_x, pos_y, player):
        self.position = (pos_x, pos_y)
        self.player = player
    
    def __lt__(self, otherPiece):
        line, col = self.position
        opLine, opCol = otherPiece.position
        return line <= opLine and col <= opCol
    def __repr__(self):
        return f"({self.position[0]},{self.position[1]}, player: {self.player})"