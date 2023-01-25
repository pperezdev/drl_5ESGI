from ..services import *
from ..constant import *
from ..worlds import *
from ..agents import *
from ..factories import *

import pygame

class Game:
    def __init__(self, world:World, agent:Agent) -> None:
        self.world = world
        self.agent = agent
        
    def display_first(self, window:pygame.Surface)-> None:
        self.world.display(window)
        self.agent.display(window)
        
    def display(self, window:pygame.Surface)-> None:
        self.world.render(window, self.agent.old_x, self.agent.old_y)
        self.agent.display(window)
        
def line_world_1x5() -> Game:
    world = open_number_world("1x5_lw.txt")
    agent = create_lineworld_agent(world.agent_spawn_x, world.agent_spawn_y)
    return Game(world, agent)

def grid_world_5x5() -> Game:
    world = open_number_world("5x5_gw.txt")
    agent = create_lineworld_agent(world.agent_spawn_x, world.agent_spawn_y)
    return Game(world, agent)

def pacman() -> Game:
    world = open_number_world("pacman.txt",tp=WorldPacMan)
    agent = create_lineworld_agent(world.agent_spawn_x, world.agent_spawn_y)
    return Game(world, agent)