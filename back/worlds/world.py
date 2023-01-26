from ..services import FileManager
from ..constant import *
from ..facades import *
import pygame


class World:
    def __init__(self, data:str, env:str, num_actions:int=2, *agrs, **kwargs) -> None:
        self.env = env
        self.agent_spawn_x = 0
        self.agent_spawn_y = 0
        
        self.green_flag_x = 0
        self.green_flag_y = 0
        
        self.red_flag_x = 0
        self.red_flag_y = 0
        
        self.num_actions = num_actions
        
        self.ground = '0'
        self.wall = '1'
        self.spawn_number = '2'
        self.green_flag = '3'
        self.red_flag = '4'
        
        self.structure = self.get_structure(data)
        self.x = len(self.structure[0]) -1
        self.y = len(self.structure) -1
    
    def reset(self):
        pass
    
    def get_num_actions(self):
        return self.num_actions
    
    def get_num_states(self):
        return (self.x+1) * (self.y+1)
    
    def render(self, window:pygame.Surface, pos_x:int, pos_y:int):
        sprite = self.structure[pos_y][pos_x]
        
        x = pos_x * sprite_size
        y = pos_y * sprite_size
        if sprite == self.ground or sprite == self.spawn_number:
            window.blit(get_basic_road(), (x,y))
        elif sprite == self.green_flag:
            window.blit(get_basic_road(), (x,y))
            window.blit(get_green_flag(), (x,y))
        elif sprite == self.red_flag:
            window.blit(get_basic_road(), (x,y))
            window.blit(get_red_flag(), (x,y))
        elif sprite == self.wall:
            window.blit(get_basic_wall(), (x,y))
            
    def display(self, window:pygame.Surface) -> None:
        for i in range(0, self.y+1):
            for j in range(0,self.x+1):
                self.render(window, j, i)
        
    def get_structure(self, data:str) -> list:
        structure = []
        for i, line in enumerate(data.split('\n')):
            for j, square in enumerate(line):
                if square == self.spawn_number:
                    self.agent_spawn_x = j
                    self.agent_spawn_y = i
                    
                if square == self.green_flag:
                    self.green_flag_x = j
                    self.green_flag_y = i
                    
                if square == self.red_flag:
                    self.red_flag_x = j
                    self.red_flag_y = i
            structure.append(line)
        return structure

    def is_wall(self, x, y) -> bool:
        if x > self.x or x < 0:
            return True
        
        if y > self.y or y < 0:
            return True
        
        if self.structure[y][x] == self.wall:
            return True
        
        return False
    
    def is_green_flag(self, x, y) -> bool:
        if self.structure[y][x] == self.green_flag:
            return True
        False
    
    def is_red_flag(self, x, y) -> bool:
        if self.structure[y][x] == self.red_flag:
            return True
        False