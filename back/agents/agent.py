from ..worlds import World
from ..constant import *
import pygame

class Agent:
    def __init__(self, x:int, y:int, sprite:pygame.Surface) -> None:
        self.old_x = x
        self.old_y = y
        self.x = x
        self.y = y
        self.sprite = sprite
    
    def can_move(self, direction_x:int, direction_y:int, world:World) -> bool:
        return not world.is_wall(direction_x, direction_y)
    
    def move(self, ud:int, rl:int, world:World):
        x = self.x + rl
        y = self.y + ud

        if self.can_move(x, y, world):
            self.old_x = self.x
            self.old_y = self.y
            self.x = x
            self.y = y
    
    def display(self, window:pygame.Surface) -> None:
        x = self.x * sprite_size
        y = self.y * sprite_size

        window.blit(self.sprite, (x, y))