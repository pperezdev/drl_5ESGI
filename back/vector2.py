import math
# import Vector2
class Vector2:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
        
<<<<<<< HEAD
    # def distance(a:Vector2, b:Vector2) -> float:
    def distance(a, b) -> float:
=======
    def distance(self, a, b) -> float:
>>>>>>> 6da4057dec953f80035a8dba9630e51e409a5f31
        num1 = (a.x - b.x)
        num2 = (a.y - b.y)
        return math.sqrt( num1 * num1 + num2 * num2)