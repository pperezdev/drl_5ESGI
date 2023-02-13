import time

import numpy as np

from back import ModelQLearning, Game


class AlgoRandom:
    def __init__(self):
        self.type_algo = "random"

    def use(self, game: Game, model: ModelQLearning, max_iteration: int, visible: bool = False) -> None:
        game.run(visible, no_event=False)

        for i in range(max_iteration):
            if game.status == "victory" or game.status == "defeat":
                break
            else:
                time.sleep(1)
                state = game.get_num_actions()
                action = np.random.choice(state)
                game.action(action)
                print(game.status)
        game.stop()
