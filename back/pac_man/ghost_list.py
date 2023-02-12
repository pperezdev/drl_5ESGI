from .ghost import Ghost
from ..agents import AgentPacman
from ..worlds import WorldPacMan

import pygame

class GhostList(list):
    def __init__(self, iterable):
        super().__init__(str(item) for item in iterable)
        
    def move(self, world:WorldPacMan, pacman:AgentPacman) -> None:
        [g.move(world, pacman) for g in self]
        
    def to_scatter(self):
        [g.on_state_scatter() for g in self]
        
    def to_chase(self):
        [g.on_state_chase() for g in self]
        
    def to_frightened(self):
        [g.on_state_frightened() for g in self]
        
    def display_first(self, window: pygame.Surface):
        [g.display_first(window) for g in self]
        
    def display(self, window: pygame.Surface):
        [g.display(window) for g in self]