from ..vector2 import Vector2

class Scatter:
    def __init__(self, target:Vector2) -> None:
        self.target = target
    
    def scatter(self) -> Vector2:
        return self.target

class ScatterBottomLeftCorner(Scatter):
     def __init__(self) -> None:
        super().__init__(Vector2(0, 36))
        
class ScatterBottomRightCorner(Scatter):
     def __init__(self) -> None:
        super().__init__(Vector2(27, 36))
        
class ScatterTopLeftCorner(Scatter):
     def __init__(self) -> None:
        super().__init__(Vector2(2, 0))
        
class ScatterTopRightCorner(Scatter):
     def __init__(self) -> None:
        super().__init__(Vector2(25, 0))