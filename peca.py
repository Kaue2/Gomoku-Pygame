import pygame

class Peca:
    def __init__(self, pos_x, pos_y, cor) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.cor = cor

    def draw(self, screen) -> None:
        if self.cor == "white":
            pygame.draw.circle(screen, self.cor, (self.pos_x, self.pos_y), 18, 0)
            pygame.draw.circle(screen, "black", (self.pos_x, self.pos_y), 18, 1)
            pygame.draw.circle(screen, "black", (self.pos_x, self.pos_y), 9, 1)
        else:
            pygame.draw.circle(screen, self.cor, (self.pos_x, self.pos_y), 18, 0)
            # teste para desenhar peça preta
            #pygame.draw.circle(screen, "white", (self.pos_x, self.pos_y), 18, 1) 
            pygame.draw.circle(screen, "white", (self.pos_x, self.pos_y), 9, 1)
