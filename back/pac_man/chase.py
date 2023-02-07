from ..agents import AgentPacman
from .ghost import Ghost
from ..vector2 import Vector2

class Chase:
    def chase(self, agent:AgentPacman, ghost:Ghost) -> Vector2:
        return Vector2(0,0)
    
class ChaseRandom(Chase):
    def __init__(self) -> None:
        super().__init__()
        self.target = Vector2(36, 0)
        
    def chase(self, agent:AgentPacman, ghost:Ghost) -> Vector2:
        dist = Vector2.distance(ghost.blinky.pos(), agent.pos())
        if dist > 8 :
            return agent.pos()
        return self.target 

class ChasePatrol(Chase):
    def chase(self, agent:AgentPacman, ghost:Ghost) -> Vector2:
        pos = ghost.pos()
        pos2 = agent.get_direction_two()

        x = (pos.x * -1) + (pos2.x*2)
        y = (pos.y * -1) + (pos2.y*2)
        return Vector2(x, y)

class ChaseAmbush(Chase):
    def chase(self, agent:AgentPacman, ghost:Ghost) -> Vector2:
        direction_hex = agent.get_direction_hex()
        pos_hex = agent.get_position_hex()
            
        direction = int(direction_hex)
        pos = int(pos_hex)

        target_global = pos + direction

        target_hex = hex(target_global)
            
        x = int(target_hex[2:2], 16) - 29
        y = (int(target_hex[0:2], 16) - 59)*-1
        target = Vector2(x, y)

        return target

class ChaseAggressive(Chase):
    def chase(self, agent:AgentPacman, ghost:Ghost) -> Vector2:
        return agent.pos()