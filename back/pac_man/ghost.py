from scatter import *
from .ghost import Ghost
from .frightened import *
from .chase import *
from .eaten import *
from ..agents import AgentPacman
from ..vector2 import Vector2

class Ghost:
    def __init__(self, chase:Chase, frightened:Frightened, scatter:Scatter, eaten:Eaten, blinky:Ghost, pacman:AgentPacman, pos:Vector2) -> None:
        self.chase = chase
        self.frightened = frightened
        self.scatter = scatter
        self.eaten = eaten
        self.blinky = blinky
        self.pacman = pacman
        self.x = pos.x
        self.y = pos.y
        
    def pos(self) -> Vector2:
        return Vector2(self.x, self.y)