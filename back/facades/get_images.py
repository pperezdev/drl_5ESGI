import pygame
from pygame.locals import * 

def get_basic_wall():
    return pygame.image.load("resources/images/wall.png").convert()

def get_basic_road():
    return pygame.image.load("resources/images/road.png").convert()

def get_basic_wall_alpha():
    return pygame.image.load("resources/images/wall.png").convert_alpha()

def get_basic_road_alpha():
    return pygame.image.load("resources/images/road.png").convert_alpha()