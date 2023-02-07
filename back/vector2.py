from .vector2 import Vector2
import math
class Vector2:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
        
    def distance(a:Vector2, b:Vector2) -> float:
        num1 = (a.x - b.x)
        num2 = (a.y - b.y)
        return math.sqrt( num1 * num1 + num2 * num2)