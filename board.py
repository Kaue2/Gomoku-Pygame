import pygame
import peca

class Board:
    def __init__(self, screen) -> None:
        self.running = True
        self.redraw = False
        self.screen = screen

    def draw_table(self) -> tuple[bool, bool]:
        for i in range(16):
            pygame.draw.line(self.screen, "black", pygame.math.Vector2(i*44, 0), pygame.math.Vector2(i*44, 748))
            pygame.draw.line(self.screen, "black", pygame.math.Vector2(0, i*44), pygame.math.Vector2(748, i*44))
        for i in range(1, 16):
            print(i)
            pygame.draw.circle(self.screen, "black", pygame.math.Vector2(i*44, 44), 3)
        pygame.display.flip()

    def handle_input(self, event) -> tuple[bool, bool]:
        self.running = True
        self.redraw = False

        match(event.type):
            case pygame.QUIT:
                self.running = False
            case pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    self.running = False
            
            case pygame.MOUSEBUTTONDOWN:
                mouseBtns = pygame.mouse.get_pressed(3)
                if mouseBtns[0]:
                    pos_x, pos_y = pygame.mouse.get_pos()
                    p = peca.Peca(pos_x, pos_y, "white")
                    p.draw(self.screen)
                    print(f"x: {pos_x}")
                    print(f"y: {pos_y}")
                    self.redraw = True

        return self.running, self.redraw