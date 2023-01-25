# Projet Deep Reinforcement Learning
5IABD2

## Équipes
- Antoine DUBOIS
- Pierrick PEREZ
- Quentin PIERSON

## Comment l'utiliser

### Lancer les jeux
Lancer les différents jeux à l'aide du fichier main.py
ou faite ceci :
```python
from back import facades

game = facades.grid_world_5x5()
#game = facades.pacman()
#game = facades.line_world_1x5()

game.run()

print(game.status)
```

le ```game.status``` vous indique l'état de la partie.
il peut avoir comme état :
- <span style="color:gray">stop</span>
- <span style="color:white">play</span>
- <span style="color:green">victory</span>
- <span style="color:red">defeat</span>


### Lancer ou visualiser les expérience
Rendez vous dans le dossier Experiments


## Contenu
### Environnement
- Line World
- Grid World
- Pac Man
- Cant Stop

### Algo

