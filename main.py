from back import facades, QLearning, ModelQLearning, DeepQLearning

#game = facades.line_world_1x5()
game = facades.grid_world_5x5()

#game.run()

#ql = DeepQLearning()

#alpha = 0.01 # taux d'apprentissage
#gamma = 0.9 # facteur de réduction
#epsilon = 0.1 # taux d'exploration
#max_iterations = 1000 # nombre maximum d'itérations
#epochs = 200

ql = DeepQLearning()

gamma = 0.99
epsilon = 0.01
learning_rate = 0.001
max_iterations = 1000
epochs = 20

#model = ql.train(game, gamma=gamma, epsilon=epsilon, learning_rate=learning_rate, max_iterations=max_iterations, epochs=epochs, debug=True)
#model.save()

#model = ql.train(game, alpha=alpha, gamma=gamma, epsilon=epsilon, max_iterations=max_iterations, epochs=epochs, debug=True)
#model.save()

model = ModelQLearning(is_keras=True)
model.load("model_gw_dqn_cd368600-9ff5-11ed-8afc-12d9bc286a40")
ql.use(game, model, visible=True)