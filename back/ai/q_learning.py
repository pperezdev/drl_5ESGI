import numpy as np
import time
from tqdm import tqdm
import uuid

from ..games import Game
from ..services import FileManager

class Model:
    def __init__(self, type_algo:str=None, env:str=None, model:np.ndarray=None):
        self.type_algo = type_algo
        self.env = env
        self.model = model
        
    def save(self, path:str=None):
        if path == None:
            path = f"model_{self.env}_{self.type_algo}_{uuid.uuid1()}"
        fm = FileManager()
        fm.save_model(path, self.model)
        
    def load(self, path):
        fm = FileManager()
        self.model = fm.load_model(path)
        
class QLearning:
    def __init__(self) -> None:
        self.type_algo = "q_learning"
        
    def train(self, game:Game, alpha:float, gamma:float, epsilon:float, max_iterations:int, epochs:int, 
              visible:bool=False, debug:bool=False) -> Model:    
        try:
            num_actions = game.get_num_actions()
            num_states = game.get_num_states()
           
            Q = np.zeros((num_states, num_actions))

            for e in tqdm(range(epochs)):
                i = 0
                break_down = False
                game.run(visible)
                time.sleep(0.3) 
                while i < max_iterations and break_down == False:
                    current_state = game.get_state()
                    
                    if np.random.uniform(0, 1) < epsilon:
                        action = np.random.choice(num_actions)
                    else:
                        action = np.argmax(Q[current_state, :])
                        
                    
                    # Exécuter l'action choisie et observer la récompense et le prochain état
                   
                    game.action(action)
                    reward = game.get_reward(e)
                    next_state = game.get_state()
                    
                    # Mettre à jour la table Q
                    Q[current_state, action] = Q[current_state, action] + alpha * (reward + gamma * np.max(Q[next_state, :]) - Q[current_state, action])
                    
                    # Vérifier si l'agent a gagné ou perdu
                    if game.status == "victory":
                        if debug:
                            print("L'agent a gagné après", i, "itérations! pos x: ", game.agent.x,  " pos y: ", game.agent.y)
                        break_down = True
                    elif game.status == "defeat":
                        if debug:
                            print("L'agent a perdu après", i,  "itérations! pos x: ", game.agent.x,  " pos y: ", game.agent.y)
                        break_down = True
                    i += 1
                game.stop()
                #print(i, break_down, e)             
            return Model(type_algo=self.type_algo, env=game.env, model=Q)
        except Exception as ex:
            print(ex)
        
    def use(self, game:Game, model:Model, visible:bool=False) -> None:
        game.run(visible, no_event=False)
        
        while game.status == "play":
            time.sleep(1)
            state = game.get_state()
            action = np.argmax(model.model[state])
            game.action(action)
            print(game.status)
        game.stop()
            