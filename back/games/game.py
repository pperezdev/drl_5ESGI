from ..worlds import *
from ..agents import *
from ..factories import *

import pygame
from pygame.locals import *
import os


class Game:
    def __init__(self, world:World, agent:Agent) -> None:
        self.world = world
        self.agent = agent
        self.status = "stop"
        self.score = 0
        self.env = world.env
        self.visible = True
        
    def get_num_actions(self) -> int:
        return self.world.get_num_actions()
    
    def get_num_states(self) -> int:
        return self.world.get_num_states()
    
    def get_reward(self, iterration:int) -> int:
        reward = 0
        if self.status == "victory":
            reward = 100
        if self.status == "defeat":
            reward = -100
        reward_tt = (self.agent.x - self.world.green_flag_x) + (self.agent.y - self.world.green_flag_y) + reward - iterration
        return reward_tt
    
    def step(self, action:int, iterration:int, type_state:bool=False):
        #regrouper les fonction action, get rewards et get_state
        self.action(action)
        reward = self.get_reward(iterration)
        if type_state:
            next_state = self.get_state()
        else:
            next_state = self.get_state_position_agent()
            
        return next_state, reward, self.status
    
    def get_state_position_agent(self) -> int: 
        val = self.agent.x + (self.agent.y * self.world.y)
        return val
    
    def get_state(self): 
        val = self.world.get_state()
        agent_pos = self.get_state_position_agent()
        val[agent_pos] = 5
        return  val
    
    def move(self, ud:int, rl:int) -> None:
        self.status = self.agent.move(ud, rl, self.world)
        if self.visible:
            self.display(self.window)
            pygame.display.flip()
            pygame.display.update()
    
    def action(self, val:int) -> str:
        if val == 0:
            self.left()
        elif val == 1:
            self.right()
        elif val == 2:
            self.up()
        else:
            self.down()
    
    def up(self) -> None:
        self.move(-1,0)
    
    def down(self) -> None:
        self.move(1,0)
        
    def left(self) -> None:
        self.move(0,-1)
        
    def right(self) -> None:
        self.move(0,1)
        
    def run(self, visible:bool=True, no_event:bool=True) -> None:
        self.reset()   
        is_visible = pygame.HIDDEN
        self.visible = visible
        if visible:
            pygame.init() 
            is_visible =pygame.SHOWN
            
            self.window = pygame.display.set_mode((1920, 1080), flags=is_visible)
            self.clock = pygame.time.Clock()
            
            self.window.fill((0, 0, 0))
            self.display_first(self.window)
                
            pygame.display.flip()
            self.status = "play"
            if no_event:
                self.__run__()
                self.stop()
        else:
            os.environ["SDL_VIDEODRIVER"] = "dummy"
    
    def reset(self) -> None:
        self.world.reset()
        self.agent.reset(self.world.agent_spawn_x, self.world.agent_spawn_y)
        self.stop()
        
    def stop(self) -> None:
        self.status = "stop"
        pygame.quit()
        
    def __run__(self) -> None:
        while self.status == "play":
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.status = "stop"
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.status = "stop"
                    elif event.key == K_RIGHT:
                        self.status = self.agent.move(0,1,self.world)
                        self.display(self.window)
                        pygame.display.flip()
                    elif event.key == K_LEFT:
                        self.status = self.agent.move(0,-1,self.world)
                        self.display(self.window)
                        pygame.display.flip()
                    elif event.key == K_UP:
                        self.status = self.agent.move(-1,0,self.world)
                        self.display(self.window)
                        pygame.display.flip()
                    elif event.key == K_DOWN:
                        self.status = self.agent.move(1,0,self.world)
                        self.display(self.window)
                        pygame.display.flip()
            pygame.display.update()
        
    def display_first(self, window:pygame.Surface)-> None:
        self.world.display(window)
        self.agent.display_first(window)
        
    def display(self, window:pygame.Surface)-> None:
        self.world.render(window, self.agent.old_x, self.agent.old_y)
        self.agent.display(window)