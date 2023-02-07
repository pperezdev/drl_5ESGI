from ..vector2 import Vector2

class Scatter:
    def __init__(self, target:Vector2) -> None:
        self.target = target
    
    def scatter(self) -> Vector2:
        return self.target

class ScatterBottomLeftCorner(Scatter):
     def __init__(self) -> None:
        super().__init__(Vector2(36, 0))
        
class ScatterBottomRightCorner(Scatter):
     def __init__(self) -> None:
        super().__init__(Vector2(36, 27))
        
class ScatterTopLeftCorner(Scatter):
     def __init__(self) -> None:
        super().__init__(Vector2(0, 2))
        
class ScatterTopRightCorner(Scatter):
     def __init__(self) -> None:
        super().__init__(Vector2(0, 25))