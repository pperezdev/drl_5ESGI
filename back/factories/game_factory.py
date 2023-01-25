from ..services import *
from ..constant import *
from ..worlds import *
from ..games import Game
from .world_factroy import *
from .agent_factory import *

def fc_line_world_1x5() -> Game:
    world = open_number_world("1x5_lw.txt")
    agent = create_lineworld_agent(world.agent_spawn_x, world.agent_spawn_y)
    return Game(world, agent)

def fc_grid_world_5x5() -> Game:
    world = open_number_world("5x5_gw.txt")
    agent = create_lineworld_agent(world.agent_spawn_x, world.agent_spawn_y)
    return Game(world, agent)

def fc_pacman() -> Game:
    world = open_number_world("pacman.txt",tp=WorldPacMan)
    agent = create_lineworld_agent(world.agent_spawn_x, world.agent_spawn_y)
    return Game(world, agent)