import pygame
from Player import HumanPlayer

class PyGameConfig:
    def __init__(self, game, scale:int = 25):
        pygame.init()
        self.name_project = 'Gomoku'
        self.background_color = (194, 147, 107)
        self.scale = scale
        self.resolution = (self.scale * 15, self.scale * 15)
        self.screen = self.create_screen()
        self.isRunning = True
        self.redraw = False
        self.clock = pygame.time.Clock()
        self.game = game
        self.game.scale = scale

    def draw_table(self) -> tuple[bool, bool]:
        for i in range(1, self.game.size + 1):
            pygame.draw.line(self.screen, "black", pygame.math.Vector2(i*self.scale, self.scale), pygame.math.Vector2(i*self.scale, self.resolution[0]))
            pygame.draw.line(self.screen, "black", pygame.math.Vector2(self.scale, i*self.scale), pygame.math.Vector2(self.resolution[0], i*self.scale))
        for i in range(1,self.game.size+1):
            for j in range(1,self.game.size+1):
                pygame.draw.circle(self.screen, "black", pygame.math.Vector2(j*self.scale, i*self.scale), 3)
        pygame.display.flip()
        
    def draw_piece(self, peca):
        color = peca.player.color
        position = (peca.position[1] + self.scale, peca.position[0] + self.scale)
        if color == "white":
            pygame.draw.circle(self.screen, color, position, 9, 0)
            pygame.draw.circle(self.screen, "black", position, 5, 1)
        else:
            pygame.draw.circle(self.screen, color, position, 9, 0)
            pygame.draw.circle(self.screen, "white", position, 5, 1) 

    def handle_play(self, p):
        self.game.play(p)  
        self.draw_piece(p)
        if(self.game.current_player.status != 'playing'):
            self.isRunning = False
        self.redraw = True

    def handle_click_button_game(self):
        pos_x, pos_y = pygame.mouse.get_pos()
        pos_x -= self.scale
        pos_y -= self.scale
        pos_x = round(pos_x / self.scale) * self.scale
        pos_y = round(pos_y / self.scale) * self.scale
        self.handle_play(self.game.current_player.create_piece_play(pos_y, pos_x))

    def handle_input(self, event) -> tuple[bool, bool]:
        self.isRunning = True
        self.redraw = False

        match(event.type):
            case pygame.QUIT:
                self.isRunning = False

            case pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    self.isRunning = False
            
            case pygame.MOUSEBUTTONDOWN:
                mouseBtns = pygame.mouse.get_pressed(3)
                if mouseBtns[0]: self.handle_click_button_game()

    def create_screen(self):
        screen = pygame.display.set_mode((self.resolution[0] + self.scale, self.resolution[1] + self.scale))
        screen.fill(self.background_color)
        pygame.display.set_caption(self.name_project)
        return screen
    
    def start_game(self):
        self.draw_table()
        while self.isRunning:
            if(type(self.game.current_player) is HumanPlayer):
                for event in pygame.event.get():
                    self.handle_input(event)  
            else:
                self.handle_play(self.game.current_player.define_an_play(self.game))
            if not self.isRunning:
                pygame.quit()
                break
            if(self.redraw):
                pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()