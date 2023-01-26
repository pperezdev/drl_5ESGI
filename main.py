from back import facades
from ai import QLearning

#game = facades.grid_world_5x5()
#game = facades.pacman()
#game = facades.line_world_1x5()

#game.run()


game = facades.line_world_1x5()
ql = QLearning()

alpha = 0.1 # taux d'apprentissage
gamma = 0.9 # facteur de réduction
epsilon = 0.1 # taux d'exploration
max_iterations = 1000 # nombre maximum d'itérations

ql.train(game, alpha=alpha, gamma=gamma, epsilon=epsilon, max_iterations=max_iterations)
