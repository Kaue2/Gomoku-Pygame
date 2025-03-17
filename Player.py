class Player:
    def __init__(self,name, color):
        self.name = name
        self.played_pieces = []
        self.color = color
    def __repr__(self):
        return f'({self.name}, {self.color}, {len(self.played_pieces)})'
