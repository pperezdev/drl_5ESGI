from enum import Enum

class MovementType(Enum):
    NOTHING = 0
    UP = 1
    LEFT = 2
    LU = 3
    DOWN = 4
    UD = 5
    LD = 6
    LUD = 7
    RIGHT = 8
    RU = 9
    LR = 10
    LRU = 11
    RD = 12
    RUD = 13
    LRD = 14
    ALL = 15