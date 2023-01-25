from ..agents import Agent
from ..facades import get_basic_agent

def create_gridworld_agent():
    pass

def create_lineworld_agent(x:int, y:int) -> Agent:
    return Agent(x, y, get_basic_agent()) 

def create_pacman_agent():
    pass

def create_cantstop_agent():
    pass