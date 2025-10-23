import random
class Coin:
    def __init__(self):
      self.__amount = 20
      self.__sideup = 'Heads' if random.randint(0, 1) == 0 else 'Tails'
    
    def toss(self):
