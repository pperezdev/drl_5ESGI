from ..worlds import World
from ..constant import *
import pygame

class Agent:
    def __init__(self, x:int, y:int, sprite_fct) -> None:
        self.old_x = x
        self.old_y = y
        self.x = x
        self.y = y
        self.sprite_fct = sprite_fct
    
    def can_move(self, direction_x:int, direction_y:int, world:World) -> bool:
        return not world.is_wall(direction_x, direction_y)
    
    def move(self, ud:int, rl:int, world:World) -> str:
        x = self.x + rl
        y = self.y + ud

        if self.can_move(x, y, world):
            self.old_x = self.x
            self.old_y = self.y
            self.x = x
            self.y = y
            
            if world.is_red_flag(self.x, self.y):
                return "defeat"
            if world.is_green_flag(self.x, self.y):
                return "victory"
            
        return "play"
    
    def display_first(self, window:pygame.Surface) -> None:
        self.sprite = self.sprite_fct()
        self.display(window)
        
    def display(self, window:pygame.Surface) -> None:
        x = self.x * sprite_size
        y = self.y * sprite_size

        window.blit(self.sprite, (x, y))