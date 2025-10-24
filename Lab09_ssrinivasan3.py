"""
Name: Shrrayash Srinivasan

Date: October 21, 2025

Description: Create a coin toss game with two players. Each player starts with 20 coins. 
Dont forget classes. Players either win or lose based on coin tosses.
"""
from coin import Coin
def main():
    print("Welcome to Match Coins games! 2 players required.")
    player_1 = Coin()
    player_2 = Coin()

    play = input("Do you want to play? Y / N: ").strip().lower()

    while play == 'y':
        player_1.toss()
        player_2.toss()

        side_1 = player_1.get_sideup()
        side_2 = player_2.get_sideup()

        print(f"Player 1 toss: {side_1}")
        print(f"Player 2 toss: {side_2}")

        if side_1 == side_2:
            print("Coins matched! Player 1 wins this round.")
            player_1.set_amount(+1)
            player_2.set_amount(-1)
        else:
            print("Coins did not match. Player 2 wins this round.")
            player_1.set_amount(-1)
            player_2.set_amount(+1)

        print(f"Player 1 coins: {player_1.get_amount()}")
        print(f"Player 2 coins: {player_2.get_amount()}")

        if player_1.get_amount() <= 0 or player_2.get_amount() <= 0:
            print("Game over! One player has run out of coins.")
            break

        play = input("Do you want to play again? Y / N: ").strip().lower()

    print("Final Results:")
    print(f"Player 1 coins: {player_1.get_amount()}")
    print(f"Player 2 coins: {player_2.get_amount()}")

    if player_1.get_amount() > player_2.get_amount():
        print("Player 1 wins!")
    elif player_2.get_amount() > player_1.get_amount():
        print("Player 2 wins!")
    else:
        print("It is a tie!")

if __name__ == "__main__":
    main()




