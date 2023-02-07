from ..agents import AgentPacman
from .ghost import Ghost
from ..vector2 import Vector2

class GhostState:
    def __init__(self) -> None:
        pass
    
class GhostStateChase(GhostState):
    def move(self, ghost:Ghost, agent:AgentPacman) -> Vector2:
        return ghost.chase.chase(agent, ghost.blinky)
    
class GhostStateEaten(GhostState):
    def move(self, ghost:Ghost, agent:AgentPacman) -> Vector2:
        return ghost.eaten.eaten()
    
class GhostStateFrightened(GhostState):
    def move(self, ghost:Ghost, agent:AgentPacman) -> Vector2:
        return ghost.frightened.frightened()
    
class GhostStateScatter(GhostState):
    def move(self, ghost:Ghost, agent:AgentPacman) -> Vector2:
        return ghost.scatter.scatter()