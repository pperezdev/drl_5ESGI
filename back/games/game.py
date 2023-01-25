from ..worlds import *
from ..agents import *
from ..factories import *

import pygame
from pygame.locals import *
import os

import asyncio
import threading

class Game:
    def __init__(self, world:World, agent:Agent) -> None:
        self.world = world
        self.agent = agent
        self.status = "stop"
        self.score = 0
    
    def move(self, ud:int, rl:int) -> None:
        self.status = self.agent.move(ud, rl, self.world)
        self.display(self.window)
        pygame.display.flip()
        
    def up(self) -> None:
        self.move(-1,0)
    
    def down(self) -> None:
        self.move(1,0)
        
    def left(self) -> None:
        self.move(0,-1)
        
    def right(self) -> None:
        self.move(0,1)
        
    def run(self, visible:bool=True, asynchrone:bool=False) -> None:    
        is_visible = pygame.HIDDEN
        
        if visible:
            is_visible =pygame.SHOWN
            
        pygame.init()
        self.window = pygame.display.set_mode((1920, 1080), flags=is_visible)
        self.clock = pygame.time.Clock()
        
        self.window .fill((0, 0, 0))
        self.display_first(self.window)
              
        pygame.display.flip()
        
        if asynchrone:
            self.thread = threading.Thread(target=self.__run__)
            self.thread.start()
        else:
            self.__run__()
            pygame.quit()
            
    def stop(self):
        pygame.quit()
        
    def __run__(self) -> None:
        self.status = "play"
        while self.status == "play":
            self.clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.status = "stop"
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.status = "stop"
                            
                    elif event.key == K_RIGHT:
                        self.status = self.agent.move(0,1,self.world)
                        self.display(self.window )
                        pygame.display.flip()
                    elif event.key == K_LEFT:
                        self.status = self.agent.move(0,-1,self.world)
                        self.display(self.window )
                        pygame.display.flip()
                    elif event.key == K_UP:
                        self.status = self.agent.move(-1,0,self.world)
                        self.display(self.window )
                        pygame.display.flip()
                    elif event.key == K_DOWN:
                        self.status = self.agent.move(1,0,self.world)
                        self.display(self.window )
                        pygame.display.flip()
        
    def display_first(self, window:pygame.Surface)-> None:
        self.world.display(window)
        self.agent.display_first(window)
        
    def display(self, window:pygame.Surface)-> None:
        self.world.render(window, self.agent.old_x, self.agent.old_y)
        self.agent.display(window)