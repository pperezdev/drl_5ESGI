from ..worlds import *
from ..agents import *
from ..pac_man import Ghost, GhostList
from ..factories import *

import pygame
from pygame.locals import *
import os

from .game import Game    

class GamePacMan(Game):

    def __init__(self, world: WorldPacMan, agent: AgentPacman, ghost_list:GhostList) -> None:
        super().__init__(world, agent)
        self.timer = 0
        self.ghost_list = ghost_list
        self.screen_x = 1200
        self.screen_y = 800
        
    def up(self) -> None:
        self.agent.hex_movement = self.agent.HEX_MOVEMENT_UP
        self.move(-1,0)
    
    def down(self) -> None:
        self.agent.hex_movement = self.agent.HEX_MOVEMENT_DOWN
        self.move(1,0)
        
    def left(self) -> None:
        self.agent.hex_movement = self.agent.HEX_MOVEMENT_LEFT
        self.move(0,-1)
        
    def right(self) -> None:
        self.agent.hex_movement = self.agent.HEX_MOVEMENT_RIGHT
        self.move(0,1)
        
    def __run__(self) -> None:
        i = 0
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
                        pygame.display.flip()
                    elif event.key == K_LEFT:
                        self.status = self.agent.move(0,-1,self.world)
                        pygame.display.flip()
                    elif event.key == K_UP:
                        self.status = self.agent.move(-1,0,self.world)
                        pygame.display.flip()
                    elif event.key == K_DOWN:
                        self.status = self.agent.move(1,0,self.world)
                        pygame.display.flip()
            i = i + 0.125      
            self.change_ghost_state(i)
            if i % 0.625 == 0:
                self.move_gost()
            self.display(self.window)
            pygame.display.update()
            
    def display_first(self, window: pygame.Surface) -> None:
        super().display_first(window)
        self.ghost_list.display_first(window)
        
    def display(self, window: pygame.Surface) -> None:
        super().display(window)
        self.ghost_list.display(window)
        [self.world.render(window, g.old_x, g.old_y) for g in self.ghost_list]
            
    def change_ghost_state(self, i):
        if i == 24.5:
            self.to_chase()
        elif i == 94.5:
            self.to_scatter()
        elif i == 119:
            self.to_chase()
        elif i == 189:
            self.to_scatter()
        elif i == 206.5:
            self.to_chase()
        elif i == 276.5:
            self.to_scatter()
        elif i == 294:
            self.to_chase()

            
    def to_scatter(self):
        self.ghost_list.to_scatter()
        
    def to_chase(self):
        self.ghost_list.to_chase()
        
    def move_gost(self):
        self.ghost_list.move(self.world, self.agent)