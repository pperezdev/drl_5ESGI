from back import facades, QLearning, Model

#game = facades.grid_world_5x5()
#game = facades.pacman()
game = facades.line_world_1x5()

game.run()

ql = QLearning()

alpha = 0.1 # taux d'apprentissage
gamma = 0.9 # facteur de réduction
epsilon = 0.1 # taux d'exploration
max_iterations = 1000 # nombre maximum d'itérations
epochs = 5

#model = ql.train(game, alpha=alpha, gamma=gamma, epsilon=epsilon, max_iterations=max_iterations, epochs=epochs)
#model.save()

#model = Model()
#model.load("model_lw_q_learning_6da045e5-9d84-11ed-b6cb-a0c589ea9759")

#ql.use(game, model, visible=True)