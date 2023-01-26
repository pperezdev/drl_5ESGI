from back import facades, QLearning, Model

#game = facades.line_world_1x5()
game = facades.grid_world_5x5()

#game.run()

ql = QLearning()

model = Model()
model.load("model_gw_q_learning_c9830ef8-9db1-11ed-a00a-a8a1598f10d9")
ql.use(game, model, visible=True)