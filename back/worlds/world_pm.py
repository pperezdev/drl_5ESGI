from ..services import FileManager
from ..constant import *
from ..facades import *
from .world import World
import pygame


class WorldPacMan(World):
    def __init__(self, data:str) -> None:
        self.agent_spawn_x = 0
        self.agent_spawn_y = 0
        self.spawn_number = '5'
        
        self.structure = self.get_structure(data)
        self.x = len(self.structure[0]) -1
        self.y = len(self.structure) -1
        
    def render(self, window:pygame.Surface, pos_x:int, pos_y:int):
        sprite = self.structure[pos_y][pos_x]
        
        x = pos_x * sprite_size
        y = pos_y * sprite_size
        
        if sprite == '0' or sprite == '5':
            window.blit(get_basic_road(), (x,y))
        if sprite == '2':
            #BALL
            #window.blit(get_green_flag(), (x,y))
            window.blit(get_basic_road(), (x,y))
        elif sprite == '3':
            window.blit(get_basic_road(), (x,y))
            #BALL
            #window.blit(get_green_flag(), (x,y))
        elif sprite == '4':
            #enemy spawn
            window.blit(get_basic_road(), (x,y))
        elif sprite == '1':
            window.blit(get_basic_wall(), (x,y))

    def is_wall(self, x, y) -> bool:
        if x > self.x or x < 0:
            return True
        
        if y > self.y or y < 0:
            return True
        
        if self.structure[y][x] == '1' or self.structure[y][x] == '4':
            return True
        
        return False