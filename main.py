from back import facades

game = facades.grid_world_5x5()
#game = facades.pacman()
#game = facades.line_world_1x5()

game.run()

print(game.status)