from ..worlds import World

class Agent:
    def __init__(self) -> None:
        pass
    
    def can_move(self, direction_x:int, direction_y:int, world:World) -> bool:
        return not world.is_wall(direction_x, direction_y)
    
    def move(self):
        pass