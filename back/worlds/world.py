from ..services import FileManager
from ..constant import *
from ..facades import *
import pygame


class World:
    def __init__(self, data:str) -> None:
        self.agent_spawn_x = 0
        self.agent_spawn_y = 0
        self.spawn_number = '2'
        
        self.structure = self.get_structure(data)
        self.x = len(self.structure[0]) -1
        self.y = len(self.structure) -1
    
    def render(self, window:pygame.Surface, pos_x:int, pos_y:int):
        sprite = self.structure[pos_y][pos_x]
        
        x = pos_x * sprite_size
        y = pos_y * sprite_size
        if sprite == '0' or sprite == '2':
            window.blit(get_basic_road(), (x,y))
        elif sprite == '3':
            window.blit(get_basic_road(), (x,y))
            window.blit(get_green_flag(), (x,y))
        elif sprite == '4':
            window.blit(get_basic_road(), (x,y))
            window.blit(get_red_flag(), (x,y))
        elif sprite == '1':
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
            structure.append(line)
        return structure

    def is_wall(self, x, y) -> bool:
        if x > self.x or x < 0:
            return True
        
        if y > self.y or y < 0:
            return True
        
        if self.structure[y][x] == 1:
            return True
        
        return False