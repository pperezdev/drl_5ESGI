from ..pac_man import *
from ..vector2 import Vector2
from ..facades import get_basic_pink, get_basic_orange, get_basic_red, get_basic_cyan

def create_all_ghost() -> GhostList:
    
    ghost_list = GhostList([])
    blinky = create_red_ghost()
    
    ghost_list.append(blinky)
    ghost_list.append(create_pink_ghost())
    ghost_list.append(create_cyan_ghost(blinky))
    ghost_list.append(create_orange_ghost())
    
    return ghost_list
    

def create_red_ghost(pos:Vector2=None) -> Ghost:
    if pos == None:
        pos = Vector2(14,15)
    ghost = Ghost(ChaseAggressive(), FrightenedWandering(), ScatterTopRightCorner(), EatenGhost(), None, pos, get_basic_red)
    ghost.on_state_scatter()
    
    return ghost

def create_pink_ghost(pos:Vector2=None) -> Ghost:
    if pos == None:
        pos = Vector2(18,14)
    ghost = Ghost(ChaseAmbush(), FrightenedWandering(), ScatterTopLeftCorner(), EatenGhost(), None, pos, get_basic_pink)
    ghost.on_state_scatter()
    
    return ghost

def create_cyan_ghost(blinky:Ghost, pos:Vector2=None) -> Ghost:
    if pos == None:
        pos = Vector2(18,15)
    ghost = Ghost(ChasePatrol(), FrightenedWandering(), ScatterBottomRightCorner(), EatenGhost(), blinky, pos, get_basic_cyan)
    ghost.on_state_scatter()
    
    return ghost

def create_orange_ghost(pos:Vector2=None) -> Ghost:
    if pos == None:
        pos = Vector2(18,12)
    ghost = Ghost(ChaseRandom(), FrightenedWandering(), ScatterBottomLeftCorner(), EatenGhost(), None, pos, get_basic_orange)
    ghost.on_state_scatter()
    ghost.blinky = ghost
    return ghost
