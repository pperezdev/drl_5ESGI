import unittest
from ..agents import Agent
from ..worlds import World

class TestAgentMethods(unittest.TestCase):
    
    def test_agent_can_move_on_0_0(self):
        a = Agent()
        w = World(10, 10)
        self.assertEquals(True, a.can_move(0, 0, w))
        
    def test_agent_can_move_on_2_2(self):
        a = Agent()
        w = World(10, 10)
        self.assertEquals(True, a.can_move(2, 2, w))
        
    def test_agent_cant_move_under_size(self):
        a = Agent()
        w = World(10, 10)
        self.assertEquals(False, a.can_move(-1, -1, w))
        
    def test_agent_cant_move_upper_size(self):
        a = Agent()
        w = World(10, 10)
        self.assertEquals(False, a.can_move(11, 11, w))