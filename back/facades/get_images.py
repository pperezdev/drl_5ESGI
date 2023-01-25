from ..constant import *

import os
import pygame
from pygame.locals import * 

def resize_alpha(path:str) -> pygame.Surface: 
    main_path  = os.path.dirname(os.path.abspath(__file__))[:-12]
    img = pygame.image.load(main_path + path).convert_alpha()
    return pygame.transform.scale(img, (sprite_size,sprite_size))
    
def resize(path:str) -> pygame.Surface: 
    main_path  = os.path.dirname(os.path.abspath(__file__))[:-12]
    img = pygame.image.load(main_path + path).convert()
    return pygame.transform.scale(img, (sprite_size,sprite_size))

def get_basic_wall() -> pygame.Surface: 
    return resize("resources/images/wall.png")

def get_basic_road() -> pygame.Surface: 
    return resize("resources/images/road.png")

def get_basic_agent() -> pygame.Surface: 
    return resize_alpha("resources/images/char.png")

def get_green_flag() -> pygame.Surface: 
    return resize_alpha("resources/images/green_flag.png")

def get_red_flag() -> pygame.Surface: 
    return resize_alpha("resources/images/red_flag.png")