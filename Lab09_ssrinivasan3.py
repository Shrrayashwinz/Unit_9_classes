"""
Name: Shrrayash Srinivasan

Date: October 21, 2025

Description: Create a coin toss game with two players. Each player starts with 20 coins. 
Dont forget classes. Players either win or lose based on coin tosses.
"""
from coin import Coin

def main ():
    print("Welcome to the coin toss game! Each player has 20 coins.")
    player_1 = coin()
    player_2 = coin()
    play = input("Do you wish to play: Y / N.")

    while play == 'y':
      player_1.toss()
      player_2.toss()

      side_1 = player_1.get_sideup()
      side_2 = player_2.get_sideup()



