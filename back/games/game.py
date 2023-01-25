from ..worlds import *
from ..agents import *
from ..factories import *

import pygame
from pygame.locals import *

class Game:
    def __init__(self, world:World, agent:Agent) -> None:
        pygame.init()
        self.world = world
        self.agent = agent
        self.status = "stop"
        self.score = 0
        
    def run(self):
        window = pygame.display.set_mode((1920, 1080))
        
        clock = pygame.time.Clock()
        i = 0
        self.status = "play"
        while self.status == "play":
            clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.status = "stop"
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.status = "stop"
                            
                    elif event.key == K_RIGHT:
                        self.status = self.agent.move(0,1,self.world)
                        self.display(window)
                        pygame.display.flip()
                    elif event.key == K_LEFT:
                        self.status = self.agent.move(0,-1,self.world)
                        self.display(window)
                        pygame.display.flip()
                    elif event.key == K_UP:
                        self.status = self.agent.move(-1,0,self.world)
                        self.display(window)
                        pygame.display.flip()
                    elif event.key == K_DOWN:
                        self.status = self.agent.move(1,0,self.world)
                        self.display(window)
                        pygame.display.flip()
            
            if i == 0:
                window.fill((0, 0, 0))
                self.display_first(window)
                i = 1
            pygame.display.flip()
        pygame.quit()
        
    def display_first(self, window:pygame.Surface)-> None:
        self.world.display(window)
        self.agent.display_first(window)
        
    def display(self, window:pygame.Surface)-> None:
        self.world.render(window, self.agent.old_x, self.agent.old_y)
        self.agent.display(window)