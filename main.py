import pygame
import board

# teste realizado com pygame
pygame.init()
screen = pygame.display.set_mode((704,748))
screen.fill((194, 147, 107))
pygame.display.set_caption("Gomoku")
currentBoard = board.Board(screen)
currentBoard.draw_table()
clock = pygame.time.Clock()

running = True
redraw = True


while running:

    for event in pygame.event.get():
        running, redraw = currentBoard.handle_input(event)
                
    if not running:
        pygame.quit()
        break
    
    if(redraw):
        pygame.display.flip()

    clock.tick(60)

pygame.quit()