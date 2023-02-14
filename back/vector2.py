import math

class Vector2:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
        
    def distance(self, a, b) -> float:
        num2 = (a.x - b.x)
        num1 = (a.y - b.y)
        return math.sqrt(num1 * num1 + num2 * num2)