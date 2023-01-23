class World:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
        self.create_world()
    
    def create_world(self)->None:
        self.env = []
        for x in range(self.x):
            env_2 = []
            for y in range(self.y):
                env_2.append(0)
            self.env.append(env_2)
            
    def is_wall(self, x, y) -> bool:
        if x > self.x or x < 0:
            return True
        
        if y > self.y or y < 0:
            return True
        
        if self.env[x][y] == 1:
            return True
        
        return False