import pygame
from pygame.locals import *
from back import get_basic_road
pygame.init()

screen = pygame.display.set_mode((640, 480))

fond = get_basic_road()
screen.blit(fond, (0,0))

running = True

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    screen.blit(fond, (0,0))
    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()
 
pygame.quit()