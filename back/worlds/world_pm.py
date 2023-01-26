from ..services import FileManager
from ..constant import *
from ..facades import *
from .world import World
import pygame


class WorldPacMan(World):
    def __init__(self, data:str, *agrs, **kwargs) -> None:
        self.env = "pc"
        self.agent_spawn_x = 0
        self.agent_spawn_y = 0
        
        self.num_actions = 4
        
        self.ground = '0'
        self.wall = '1'
        self.ball = '2'
        self.mega_ball = '3'
        self.enemy_spawn = '4'
        self.spawn_number = '5'
        
        self.green_flag = '9'
        self.red_flag = '8'
    
        self.structure = self.get_structure(data)
        self.x = len(self.structure[0]) -1
        self.y = len(self.structure) -1
        
    def render(self, window:pygame.Surface, pos_x:int, pos_y:int):
        sprite = self.structure[pos_y][pos_x]
        
        x = pos_x * sprite_size
        y = pos_y * sprite_size
        
        if sprite == self.ground or sprite == self.spawn_number:
            window.blit(get_basic_road(), (x,y))
        if sprite == self.ball:
            #BALL
            #window.blit(get_green_flag(), (x,y))
            window.blit(get_basic_road(), (x,y))
        elif sprite == self.mega_ball:
            window.blit(get_basic_road(), (x,y))
            #BALL
            #window.blit(get_green_flag(), (x,y))
        elif sprite == self.enemy_spawn:
            #enemy spawn
            window.blit(get_basic_road(), (x,y))
        elif sprite == self.wall:
            window.blit(get_basic_wall(), (x,y))

    def is_wall(self, x, y) -> bool:
        if x > self.x or x < 0:
            return True
        
        if y > self.y or y < 0:
            return True
        
        if self.structure[y][x] == self.wall or self.structure[y][x] == self.enemy_spawn:
            return True
        
        return False