from .scatter import *
from .ghost_state import *
from .frightened import *
from .chase import *
from ..constant import *
from .eaten import *
from ..agents import AgentPacman
from ..vector2 import Vector2
from ..worlds import WorldPacMan
from .movement_type import MovementType

import pygame

class Ghost:
    MAX_NUMBER = 15
    MOVE_SPEED_NORMAL = 0.25
    MOVE_SPEED_CHASE = 0.17
    MOVE_SPEED_EATEN = 0.1
    
    def __init__(self, chase:Chase, frightened:Frightened, scatter:Scatter, eaten:Eaten, blinky, pos:Vector2, sprite_fct) -> None:
        self.move_speed = self.MOVE_SPEED_NORMAL
        self.ghost_state = GhostState()
        self.chase = chase
        self.frightened = frightened
        self.scatter = scatter
        self.eaten = eaten
        self.blinky = blinky
        self.old_x = pos.x
        self.old_y = pos.y
        self.x = pos.x
        self.y = pos.y
        self.last_movement = MovementType.DOWN
        self.sprite_fct = sprite_fct
        
    def pos(self) -> Vector2:
        return Vector2(self.x, self.y)
    
    def move(self, world:WorldPacMan, pacman:AgentPacman) -> None:
        target = self.ghost_state.move(self, pacman)
        number = self.MAX_NUMBER
        
        vU = Vector2(self.x  - 1, self.y)
        vL = Vector2(self.x  , self.y- 1)
        vD = Vector2(self.x  + 1, self.y)
        vR = Vector2(self.x , self.y + 1)
        
        if vL.y == 18 or vR.y == 18: 
            
            if vR.x == 28 and self.last_movement == MovementType.LEFT:
                self.x = 0
                self.y = 18

            if vL.x == -1 and self.last_movement == MovementType.RIGHT:
                self.x = 27
                self.y = 18
        
        if world.is_wall(vR.x, vR.y) or self.last_movement == MovementType.RIGHT: 
            number -= int(MovementType.RIGHT._value_)
            
        if world.is_wall(vL.x, vL.y) or self.last_movement == MovementType.LEFT: 
            number -= int(MovementType.LEFT._value_)
            
        if world.is_wall(vU.x, vU.y) or self.last_movement == MovementType.UP: 
            number -= int(MovementType.UP._value_)
            
        if world.is_wall(vD.x, vD.y) or self.last_movement == MovementType.DOWN or world.is_spawn(vD.x, vD.y):
            number -= int(MovementType.DOWN._value_)

        pos = self.movement(number, target, vU, vL, vD, vR)
        self.old_x = self.x
        self.old_y = self.y
        self.x = pos.x
        self.y = pos.y
            
    def movement(self, movement_type:MovementType, target:Vector2, 
                 vU:Vector2, vL:Vector2, vD:Vector2, vR:Vector2) -> Vector2:
        u = Vector2.distance(None, vU, target)
        l = Vector2.distance(None, vL, target)
        d = Vector2.distance(None, vD, target)
        r = Vector2.distance(None, vR, target)

        if MovementType.LD._value_ == movement_type:
            if l <= d:
                self.last_movement = MovementType.RIGHT
                return vL
                    
            self.last_movement = MovementType.UP
            return vD
                
        if MovementType.LR._value_ == movement_type:
            if l <= r:
                self.last_movement = MovementType.RIGHT
                return vL
                    
            self.last_movement = MovementType.LEFT
            return vR
                
        if MovementType.LU._value_ == movement_type:
            if u <= l:
                self.last_movement = MovementType.DOWN
                return vU
                    
            self.last_movement = MovementType.RIGHT
            return vL
                
        if MovementType.RD._value_ == movement_type:
            if d <= r:
                self.last_movement = MovementType.UP
                return vD
                    
            self.last_movement = MovementType.LEFT
            return vR
                
        if MovementType.RU._value_ == movement_type:
            if u <= r:
                self.last_movement = MovementType.DOWN
                return vU
                    
            self.last_movement = MovementType.LEFT
            return vR
                
        if MovementType.UD._value_ == movement_type:
            if u <= d:
                self.last_movement = MovementType.DOWN
                return vU
                    
            self.last_movement = MovementType.UP
            return vD
                
        if MovementType.LRD._value_ == movement_type:
            if l <= r and l <= d:
                self.last_movement = MovementType.RIGHT
                return vL
                    
            if d <= r:
                self.last_movement = MovementType.UP
                return vD
                    
            self.last_movement = MovementType.LEFT
            return vR
        
        if MovementType.LRU._value_ == movement_type:
            if u <= l and u <= r:
                self.last_movement = MovementType.DOWN
                return vU
                    
            if l <= r:
                self.last_movement = MovementType.RIGHT
                return vL
                    
            self.last_movement = MovementType.LEFT
            return vR
        if MovementType.LUD._value_ == movement_type:
            if u <= l and u <= d:
                self.last_movement = MovementType.DOWN
                return vU
                    
            if l <= d:
                self.last_movement = MovementType.RIGHT
                return vL
                    
            self.last_movement = MovementType.UP
            return vD
        if MovementType.RUD._value_ == movement_type:
            if u <= d and u <= r:
                self.last_movement = MovementType.DOWN
                return vU
                    
            if d <= r:
                self.last_movement = MovementType.UP
                return vD
                    
            self.last_movement = MovementType.LEFT
            return vR
        if MovementType.ALL._value_ == movement_type:
            if u <= d and u <= r and u <= l:
                self.last_movement = MovementType.DOWN
                return vU
                    

            if l <= d and l <= r:
                self.last_movement = MovementType.RIGHT
                return vL
                    
            if d <= r:
                self.last_movement = MovementType.UP
                return vD
                    
            self.last_movement = MovementType.LEFT
            return vR
        if MovementType.UP._value_ == movement_type:
            self.last_movement = MovementType.DOWN
            return vU
        
        if MovementType.LEFT._value_ == movement_type:
            self.last_movement = MovementType.RIGHT
            return vL
        
        if MovementType.DOWN._value_ == movement_type:
            self.last_movement = MovementType.UP
            return vD
        if MovementType.RIGHT._value_ == movement_type:
            self.last_movement = MovementType.LEFT
            return vR
                
            
        return Vector2(0, 0)
    
    
    def on_state_chase(self) -> None:
        self.ghost_state = GhostStateChase()
        self.move_speed = self.MOVE_SPEED_CHASE
        self.last_movement = MovementType.NOTHING
        
        
    def on_state_frightened(self) -> None:
        self.ghost_state = GhostStateFrightened()
        self.move_speed = self.MOVE_SPEED_NORMAL
        self.last_movement = MovementType.NOTHING


    def on_state_scatter(self) -> None:
        self.ghost_state = GhostStateScatter()
        self.move_speed = self.MOVE_SPEED_NORMAL
        self.last_movement = MovementType.NOTHING
        
        
    def on_state_eaten(self) -> None:
        self.ghost_state = GhostStateEaten()
        self.move_speed = self.MOVE_SPEED_EATEN
        self.last_movement = MovementType.NOTHING
        
    def display_first(self, window:pygame.Surface) -> None:
        self.sprite = self.sprite_fct()
        self.display(window)
        
    def display(self, window:pygame.Surface) -> None:
        x = self.x * sprite_size
        y = self.y * sprite_size

        window.blit(self.sprite, (x, y))