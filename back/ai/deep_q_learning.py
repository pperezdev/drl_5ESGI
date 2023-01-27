import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Input
from keras.optimizers import Adam
import random

from .model import ModelQLearning

import time
from tqdm import tqdm
from ..games import Game

class DeepQLearning:    
    def __init__(self) -> None:
        self.type_algo = "dqn"
    
    def __build_model(self, learning_rate:float, num_actions:int, num_states:int) -> Sequential:
        # Neural Net for Deep-Q learning Model
        model = Sequential()
        model.add(Dense(24, input_dim=num_states, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(num_actions, activation='linear'))
        model.compile(loss='mse',
                      optimizer=Adam(lr=learning_rate))
        return model

    def epsilon_greedy(self, state:int, epsilon:float, model: Sequential, num_actions:int):
        if np.random.rand() <= epsilon:
            return random.randrange(num_actions)
        act_values = model.predict(state)
        return np.argmax(act_values[0]) 
    
    def train(self, game:Game, gamma:float, epsilon:float, 
              learning_rate:float, max_iterations:int, epochs:int, 
              visible:bool=False, debug:bool=False) -> ModelQLearning:
        num_actions = game.get_num_actions()
        num_states = game.get_num_states()
        
        model = self.__build_model(learning_rate, num_actions, num_states)
        
        for e in tqdm(range(epochs)):
            game.run(visible)
            break_down = False
            i = 0
            state = game.get_state()
            state = np.reshape(state, [1, num_states])
            
            while i < max_iterations and break_down == False:
                action = self.epsilon_greedy(state, epsilon, model, num_actions)
                
                next_state, reward, status = game.step(action, i, type_state=True)
                next_state = np.reshape(next_state, [1, num_states])

                target = reward
                if not break_down:
                    target = reward + gamma * np.amax(model.predict(next_state)[0])
                target_f = model.predict(state)
                target_f[0][action] = target
                model.fit(state, target_f, epochs=1, verbose=0)
                
                state = next_state
                if status == "victory" or status == "defeat":
                    if debug:
                        print(status, i, "itérations! pos x:", game.agent.x,  "pos y:", game.agent.y, "reward:", reward)
                    break_down = True
                i += 1
            game.stop()
        return ModelQLearning(self.type_algo, env=game.env, model=model)
            
    def use(self, game:Game, model:ModelQLearning, visible:bool=False) -> None:
        game.run(visible, no_event=False)
        
        while game.status == "play":
            time.sleep(1)
            state = game.get_state()
            action = np.argmax(model.model[state])

            game.action(action)
            print(game.status)
        game.stop()