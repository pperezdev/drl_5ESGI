from ..vector2 import Vector2

class Eaten:
    def eaten(self) -> Vector2:
        return Vector2(0,0)
    
class EatenGhost(Eaten):
    def eaten(self) -> Vector2:
        return Vector2(0,0)