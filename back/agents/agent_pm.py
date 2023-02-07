from .agent import Agent
from ..vector2 import Vector2

class AgentPacman(Agent):
    
    HEX_MOVEMENT_UP = "03FC"
    HEX_MOVEMENT_DOWN = "0004"
    HEX_MOVEMENT_LEFT = "0400"
    HEX_MOVEMENT_RIGHT = "FC00"
    
    def __init__(self, x: int, y: int, sprite_fct) -> None:
        super().__init__(x, y, sprite_fct)
        self.direction = Vector2(0,0)
        self.hex_movement = ""
        
    def get_direction_two(self) -> Vector2:
        return self.direction
    
    def get_position_hex(self) -> str:
        x_sbyte = (4 + 29).to_bytes(2, byteorder='big').hex()
        y_sbyte = ((9 - 59)*-1).to_bytes(2, byteorder='big').hex()
        return x_sbyte + y_sbyte
    
    def get_direction_hex(self) -> str:
        return self.hex_movement