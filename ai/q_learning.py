import numpy as np
import time
import tqdm

class QLearning:
    def __init__(self) -> None:
        pass
        
    def train(self, game, alpha:float, gamma:float, epsilon:float, max_iterations:int, epochs:int):    
        num_actions = game.get_num_actions()
        
        Q = np.zeros((game.get_num_states(), num_actions))
        for e in tqdm(range(epochs)):
            game.run(visible=False, asynchrone=True)
            for i in range(max_iterations):
                current_state = game.get_state()
                
                if np.random.uniform(0, 1) < epsilon:
                    action = np.random.choice(num_actions)
                else:
                    action = np.argmax(Q[current_state, :])
                
                # Exécuter l'action choisie et observer la récompense et le prochain état
                game.action(action)
                reward = game.get_reward()
                next_state = game.get_state()
                
                # Mettre à jour la table Q
                Q[current_state, action] = Q[current_state, action] + alpha * (reward + gamma * np.max(Q[next_state, :]) - Q[current_state, action])
                
                # Vérifier si l'agent a gagné ou perdu
                if game.status == "victory":
                    print("L'agent a gagné après", i, "itérations!")
                    break
                elif game.status == "defeat":
                    print("L'agent a perdu après", i, "itérations.")
                    break
                
                time.sleep(game.clock.tick(30)/100) 
            game.stop()