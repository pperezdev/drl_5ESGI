import numpy as np
import time
from tqdm import tqdm
from .model import ModelQLearning

from ..games import Game

class QLearning:
    def __init__(self) -> None:
        self.type_algo = "q_learning"
        
    def train(self, game:Game, alpha:float, gamma:float, epsilon:float, max_iterations:int, epochs:int, 
              visible:bool=False, debug:bool=False) -> ModelQLearning:    
        
        num_actions = game.get_num_actions()
        num_states = game.get_num_states()
           
        Q = np.zeros((num_states, num_actions))

        for e in tqdm(range(epochs)):
            i = 0
            break_down = False
            game.run(visible)
            while i < max_iterations and break_down == False:
                current_state = game.get_state_position_agent()
                #current_state = np.reshape(current_state, [1, num_states])
                
                if np.random.uniform(0, 1) < epsilon:
                    action = np.random.choice(num_actions)
                else:
                    action = np.argmax(Q[current_state, :])
                    
                # Exécuter l'action choisie et observer la récompense et le prochain état

                next_state, reward, status = game.step(action, i)
                #next_state = np.reshape(next_state, [1, num_states])

                # Mettre à jour la table Q
                Q[current_state, action] = Q[current_state, action] + alpha * (reward + gamma * np.max(Q[next_state, :]) - Q[current_state, action])
                
                # Vérifier si l'agent a gagné ou perdu
                if status == "victory" or status == "defeat":
                    if debug:
                        print(status, i, "itérations! pos x: ", game.agent.x,  " pos y: ", game.agent.y, " reward: ", reward)
                    break_down = True
                i += 1
            game.stop()
                             
        return ModelQLearning(type_algo=self.type_algo, env=game.env, model=Q)

        
    def use(self, game:Game, model:ModelQLearning, visible:bool=False) -> None:
        game.run(visible, no_event=False)
        
        while game.status == "play":
            time.sleep(1)
            state = game.get_state_position_agent()
            action = np.argmax(model.model[state])
            game.action(action)
            print(game.status)
        game.stop()
            