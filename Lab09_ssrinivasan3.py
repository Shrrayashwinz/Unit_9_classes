"""
Name: Shrrayash Srinivasan

Date: October 21, 2025

Description: Create a coin toss game with two players. Each player starts with 20 coins. 
Dont forget classes. Players either win or lose based on coin tosses.
"""

import random
class Coin:
    def __init__(self):
      self.__amount = 20
      self.__sideup = 'Heads' if random.randint(0, 1) == 0 else 'Tails'
    
    def toss(self):


    

def main ():
    print("Welcome to the coin toss game! Each player has 20 coins.")
    player_1 = coin()
    player_2 = coin()
