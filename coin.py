"""
Program Name: coin.py
Author: Shrrayash Srinivasan
Purpose: Defines the Coin class for the Match Coins game, including toss logic and coin tracking.
Date: October 23, 2025
"""

import random
class Coin:
    def __init__(self):
        self.__amount = 20
        self.__sideup = random.choice(['Heads', 'Tails'])
      
    
    def toss(self):
        self.__sideup = 'Heads' if random.randint(0,1) == 0 else 'Tails'
    
    def get_sideup(self):
        return self.__sideup
    
    def set_amount(self, change):
        self.__amount += change
    
    def get_amount(self):
        return self.__amount










    

    
    

      





