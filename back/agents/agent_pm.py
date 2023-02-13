from .agent import Agent
from ..vector2 import Vector2
from ..worlds import World

class AgentPacman(Agent):
    
    HEX_MOVEMENT_UP = "03FC"
    HEX_MOVEMENT_DOWN = "0004"
    HEX_MOVEMENT_LEFT = "0400"
    HEX_MOVEMENT_RIGHT = "FC00"
    
    def __init__(self, x: int, y: int, sprite_fct) -> None:
        super().__init__(x, y, sprite_fct)
        self.direction = Vector2(0,0)
        self.hex_movement = self.HEX_MOVEMENT_UP
        
    def move(self, ud:int, rl:int, world:World) -> str:
        x = self.x + rl
        y = self.y + ud

        if self.can_move(x, y, world):
            if x == -1:
                x = 27
            if x > world.x:
                x = 0

            self.old_x = self.x
            self.old_y = self.y
            self.x = x
            self.y = y
                
        return "play"
        
    def get_direction_two(self) -> Vector2:
        return self.direction
    
    def get_position_hex(self) -> str:
        x_sbyte = self.x + 29
        y_sbyte = (self.y -  59)*-1
        result = x_sbyte + y_sbyte
        return result.to_bytes(2, byteorder='big').hex()
    
    def get_direction_hex(self) -> str:
        return self.hex_movement