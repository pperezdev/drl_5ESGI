import pygame
from pygame.locals import *
from back import facades
pygame.init()

window = pygame.display.set_mode((1920, 1080))
game = facades.designed_map.pacman()
running = True
clock = pygame.time.Clock()
i = 0
while running:
    clock.tick(30)
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
					
            elif event.key == K_RIGHT:
                game.agent.move(0,1,game.world)
                game.display(window)
                pygame.display.flip()
            elif event.key == K_LEFT:
                game.agent.move(0,-1,game.world)
                game.display(window)
                pygame.display.flip()
            elif event.key == K_UP:
                game.agent.move(-1,0,game.world)
                game.display(window)
                pygame.display.flip()
            elif event.key == K_DOWN:
                game.agent.move(1,0,game.world)
                game.display(window)
                pygame.display.flip()
    # Fill the background with white
    
    if i == 0:
        window.fill((0, 0, 0))
        game.display_first(window)
        i = 1
    pygame.display.flip()
pygame.quit()