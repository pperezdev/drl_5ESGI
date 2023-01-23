import random
class DiceComb:
    def __init__(self, dice_one:int, dice_two:int, combi:int) -> None:
        self.dice_one = dice_one
        self.dice_two = dice_two
        self.combi = combi
class Dice:
    def random_dice(self) -> int:
        return random.randint(1, 7)
    
    def play(self):
        dices = []
        comblist = []
        dicecomblist = []
        for i in range(0, 4):
            dices[i] = self.random_dice()
        
        for i in range(0, 4):
            for j in range(0, 4):
                if i == j:
                    continue
                
                num = dices[i] + dices[j]
                dc = DiceComb(dices[i], dices[j], num)
                dicecomblist.append(dc)
                
                if num not in comblist:
                    comblist.append(num)
        
        return dicecomblist