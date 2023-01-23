import unittest
from ..agents import Agent
from ..worlds import World

class TestAgentMethods(unittest.TestCase):
    
    def test_agent_can_move(self):
        a = Agent()
        w = World(10, 10)
        self.assertEquals(True, a.can_move(2, 2, w))