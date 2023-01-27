from back import facades, QLearning, ModelQLearning

#game = facades.line_world_1x5()
game = facades.grid_world_5x5()

#game.run()

ql = QLearning()

alpha = 0.01 # taux d'apprentissage
gamma = 0.9 # facteur de réduction
epsilon = 0.1 # taux d'exploration
max_iterations = 1000 # nombre maximum d'itérations
epochs = 200

#model = ql.train(game, alpha=alpha, gamma=gamma, epsilon=epsilon, max_iterations=max_iterations, epochs=epochs, debug=True)
#model.save()

model = ModelQLearning()
model.load("model_gw_q_learning_3abeab70-9e39-11ed-b81c-a8a1598f10d9")
ql.use(game, model, visible=True)