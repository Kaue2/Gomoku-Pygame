import pygame
from Peca import Peca
from Game import Game

class PyGameConfig:
    def __init__(self, game:Game):
        pygame.init()
        self.name_project = 'Gomoku'
        self.background_color = (194, 147, 107)
        self.resolution = (600,600)
        self.screen = self.create_screen()
        self.isRunning = True
        self.redraw = False
        self.clock = pygame.time.Clock()
        self.game = game

    def draw_table(self) -> tuple[bool, bool]:
        for i in range(16):
            pygame.draw.line(self.screen, "black", pygame.math.Vector2(i*44, 0), pygame.math.Vector2(i*44, 748))
            pygame.draw.line(self.screen, "black", pygame.math.Vector2(0, i*44), pygame.math.Vector2(748, i*44))
        for i in range(1, 16):
            pygame.draw.circle(self.screen, "black", pygame.math.Vector2(i*44, 44), 3)
        pygame.display.flip()
        
    def draw_piece(self, peca:Peca):
        color = peca.player.color
        position = peca.position
        position = sorted(position, reverse=True)
        if color == "white":
            pygame.draw.circle(self.screen, color, position, 18, 0)
            pygame.draw.circle(self.screen, "black", position, 18, 1)
            pygame.draw.circle(self.screen, "black", position, 9, 1)
        else:
            pygame.draw.circle(self.screen, color, position, 18, 0)
            # teste para desenhar peça preta
            #pygame.draw.circle(self.screen, "white", position, 18, 1) 
            pygame.draw.circle(self.screen, "white", position, 9, 1)

    def handle_input(self, event) -> tuple[bool, bool]:
        self.isRunning = True
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
                    pos_x = round(pos_x / 25) * 25
                    pos_y = round(pos_y / 25) * 25
                    p = Peca(pos_y,pos_x, self.game.current_player)
                    if(self.game.play(p) == 'ok'):
                        self.draw_piece(p)
                    self.redraw = True

    def create_screen(self):
        screen = pygame.display.set_mode(self.resolution)
        screen.fill(self.background_color)
        pygame.display.set_caption(self.name_project)
        return screen
    
    def start_game(self):
        self.draw_table()
        while self.isRunning:
            for event in pygame.event.get():
                self.handle_input(event)  
            if not self.isRunning:
                pygame.quit()
                break
            if(self.redraw):
                pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()