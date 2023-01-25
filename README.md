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
```

le ```game.status``` vous indique l'état de la partie.
il peut avoir comme état :
- <span style="color:gray">stop</span>
- <span style="color:white">play</span>
- <span style="color:green">victory</span>
- <span style="color:red">defeat</span>

Vous pouvez ensuite utiliser les fonctions si dessous pour faire 
bouger votre agent :
- ```game.up()```
- ```game.down()```
- ```game.right()```
- ```game.left()```

### Lancer ou visualiser les expérience
Rendez vous dans le dossier Experiments

Voici un exemple d'experiment :
```python
import sys
import time

sys.path.append('..')

from back import facades

game = facades.line_world_1x5()

game.run(visible=False, asynchrone=True)

while game.thread.is_alive():
    game.right()
    print(game.status)
    time.sleep(game.clock.tick(30)/100)
game.stop()

```


## Contenu
### Environnement
- Line World
- Grid World
- Pac Man
- Cant Stop

### Algo

