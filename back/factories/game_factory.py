from ..services import *
from ..constant import *
from ..worlds import *
from ..games import Game, GamePacMan
from .world_factroy import *
from .agent_factory import *
from .ghost_factory import *

def fc_line_world_1x5() -> Game:
    world = open_number_world("1x5_lw.txt", env='lw')
    agent = create_lineworld_agent(world.agent_spawn_x, world.agent_spawn_y)
    return Game(world, agent)

def fc_grid_world_5x5() -> Game:
    world = open_number_world("5x5_gw.txt", num_actions = 4, env='gw')
    agent = create_lineworld_agent(world.agent_spawn_x, world.agent_spawn_y)
    return Game(world, agent)

def fc_pacman() -> GamePacMan:
    world = open_number_world("pacman.txt",tp=WorldPacMan)
    agent = create_pacman_agent(world.agent_spawn_x, world.agent_spawn_y)
    ghost_list = create_all_ghost()
    return GamePacMan(world, agent, ghost_list)